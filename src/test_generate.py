"""Offline regression tests. Never invoke git, push, or production publishing."""
import copy
import html
import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

import generate as G
import multibook as MB
from locales import LOCALES, route


class Tags(HTMLParser):
    def __init__(self, document):
        super().__init__()
        self.tags = []
        self.feed(document)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def attrs(self, tag):
        return [attrs for name, attrs in self.tags if name == tag]


class LanguageTests(unittest.TestCase):
    def setUp(self):
        revision_patch = patch.object(G.C, 'REVISION_SET', '')
        revision_patch.start()
        self.addCleanup(revision_patch.stop)
        self.collection = {lang: G.load_chapters(lang) for lang in LOCALES}
        # Test pending/approved states in memory, independently of future human approvals.
        for lang in ('tr', 'yue', 'ko'):
            for chapter in self.collection[lang]:
                chapter['approved'] = False
        # 多书页同样按"只有英文已批准"来测，不依赖真实译本状态。
        real_book_loader = MB.load_chapters
        self.addCleanup(setattr, MB, 'load_chapters', real_book_loader)

        def pending_book_loader(slug, language='en'):
            chapters = real_book_loader(slug, language)
            return [dict(c, approved=(language == 'en' and c['approved'])) for c in chapters]
        MB.load_chapters = pending_book_loader

    def build(self, preview=False, collection=None):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        output = Path(temporary.name)
        with patch.object(G.C, 'OUTPUT_DIR', str(output)), patch.object(G.C, 'PREVIEW_DRAFTS', preview):
            fixtures = collection if collection is not None else self.collection
            with patch.object(G, 'load_chapters', side_effect=lambda lang: fixtures[lang]):
                G.main()
        return output

    def test_translation_content_and_sources(self):
        for lang in ('tr', 'yue', 'ko'):
            chapters = G.load_chapters(lang)
            self.assertGreaterEqual(len(chapters), 3)
            for translation in chapters:
                self.assertIn(translation['status'], ('ai-draft', 'approved'))
                meta = G.read_doc(translation['path'])[0]
                source = G.CHAPTERS_DIR / translation['path'].name
                self.assertRegex(meta['source_sha256'], r'^[a-f0-9]{64}$')
                if translation['approved']:
                    self.assertEqual(meta['source_sha256'], G.source_digest(source))
                self.assertNotEqual(translation['html'], G.read_doc(source)[2])
                self.assertGreater(translation['words'], 0)

    def test_english_approval_does_not_approve_translation(self):
        meta = {'status': 'ai-draft', 'source_sha256': 'hash'}
        self.assertFalse(G.translation_approved(meta, {'status': 'approved'}, 'hash'))
        meta['status'] = 'approved'
        self.assertFalse(G.translation_approved(meta, {'status': 'approved'}, 'hash'))

    def test_source_change_and_draft_block_translation(self):
        meta = {'status': 'approved', 'source_sha256': 'hash', 'reviewer': 'TEST ONLY',
                'review_date': '2026-11-23', 'review_notes': 'Fixture-only review, never written to repository.'}
        self.assertTrue(G.translation_approved(meta, {'status': 'approved'}, 'hash'))
        self.assertFalse(G.translation_approved(meta, {'status': 'approved'}, 'changed'))
        self.assertFalse(G.translation_approved(meta, {'status': 'ai-draft'}, 'hash'))

    def test_production_hides_drafts(self):
        output = self.build()
        for lang in ('tr', 'yue', 'ko'):
            for c in self.collection[lang]:
                document = (output / G.chapter_path(c).strip('/') / 'index.html').read_text()
                self.assertIn('content="noindex,follow"', document)
                self.assertNotIn(c['html'], document)
                self.assertNotIn('application/ld+json', document)
                self.assertNotIn('hreflang=', document)

    def test_production_sitemap_excludes_pending_languages(self):
        output = self.build()
        root = ET.parse(output / 'sitemap.xml').getroot()
        urls = [item.text for item in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
        # 2 (en home/about) + approved en chapters + 4 evergreen pages x indexable languages
        # + 2 entry pages of the summary-edition language (yue home/about only).
        indexable_langs = [lg for lg in LOCALES if lg not in G.C.SUMMARY_LANGS]
        evergreen_count = len(G.EV.PAGES) * len(indexable_langs)
        summary_entry = sum(2 for lg in G.C.SUMMARY_LANGS
                            if any(c['approved'] for c in self.collection[lg]))
        # editorial pages: glossary index + glossary terms + act pages + companion pages
        editorial = 1 + len(G.GX.ORDER) + len(G.AX.ACTS) + len(G.XT.ORDER)
        expected = (2 + sum(c['approved'] for c in self.collection['en'])
                    + evergreen_count + summary_entry + editorial
                    + len(MB.sitemap_paths()))
        self.assertEqual(len(urls), expected)
        for url in urls:
            path = urlparse(url).path
            document = (output / path.strip('/') / 'index.html').read_text()
            self.assertIn('content="index,follow"', document)
        # No *chapter* of a pending translation language enters the sitemap
        # (evergreen companion pages legitimately do).
        for lang in ('tr', 'yue', 'ko'):
            for c in self.collection[lang]:
                if not c['approved']:
                    self.assertNotIn(G.chapter_path(c), urls)

    def test_enriched_home_structure(self):
        output = self.build()
        for lang in LOCALES:
            document = (output / route(lang).strip('/') / 'index.html').read_text()
            # Explore menu with links to all four companion pages.
            self.assertIn('class="explore"', document)
            for slug in G.EV.PAGES:
                self.assertIn(f'href="{route(lang, f"/{slug}/")}"', document)
            # Three-part grouping labels (English always has approved chapters).
            if lang == 'en':
                for label in G.EXTRA[lang]['parts']:
                    self.assertIn(html.escape(label), document)
            # Reading-progress hooks present.
            self.assertIn('data-page-kind="home"', document)
            self.assertIn('data-resume', document)
            self.assertIn('data-progress', document)
            if lang == 'en':
                self.assertIn('data-chapter=', document)

    def test_enriched_chapter_pages(self):
        output = self.build()
        c = self.collection['en'][5]  # chapter 6 -> themes + world
        document = (output / G.chapter_path(c).strip('/') / 'index.html').read_text()
        self.assertIn('data-page-kind="chapter"', document)
        self.assertIn(f'data-chapter-num="{c["num"]}"', document)
        self.assertIn(G.EXTRA['en']['further'], document)
        # Breadcrumb + Chapter schemas.
        raw = [json.loads(x) for x in
               re.findall(r'<script type="application/ld\+json">(.*?)</script>', document, re.S)]
        schemas = [item for block in raw for item in (block if isinstance(block, list) else [block])]
        types = [s.get('@type') for s in schemas]
        self.assertIn('BreadcrumbList', types)
        self.assertIn('Chapter', types)

    def test_faq_schema(self):
        output = self.build()
        for lang in [lg for lg in LOCALES if lg not in G.C.SUMMARY_LANGS]:
            document = (output / route(lang, '/faq/').strip('/') / 'index.html').read_text()
            raw = [json.loads(x) for x in
                   re.findall(r'<script type="application/ld\+json">(.*?)</script>', document, re.S)]
            schemas = [item for block in raw for item in (block if isinstance(block, list) else [block])]
            faq = next((s for s in schemas if s.get('@type') == 'FAQPage'), None)
            self.assertIsNotNone(faq, lang)
            self.assertEqual(len(faq['mainEntity']), len(G.EV.CONTENT[lang]['faq']))
            for q in faq['mainEntity']:
                self.assertEqual(q['@type'], 'Question')
                self.assertIn('acceptedAnswer', q)

    def test_evergreen_pages(self):
        output = self.build()
        expected_slugs = tuple(G.EV.PAGES)
        for lang in LOCALES:
            for slug in expected_slugs:
                path = route(lang, f"/{slug}/")
                document = (output / path.strip('/') / 'index.html').read_text()
                if lang in G.C.SUMMARY_LANGS:
                    # 节录语言：可读但不进索引，也不参与 hreflang 集群
                    self.assertIn('content="noindex,follow"', document)
                    self.assertNotIn('hreflang=', document)
                    self.assertIn(html.escape(G.EV.TITLES[slug][lang]), document)
                    continue
                self.assertIn('content="index,follow"', document)
                self.assertIn(f'<html lang="{LOCALES[lang]["lang"]}"', document)
                self.assertIn(html.escape(G.EV.TITLES[slug][lang]), document)
                tags = Tags(document)
                # Reciprocal hreflang across all four languages for this page.
                alts = {a['hreflang']: a['href'] for a in tags.attrs('link') if a.get('rel') == 'alternate' and 'hreflang' in a}
                for other in LOCALES:
                    if other in G.C.SUMMARY_LANGS:
                        continue
                    self.assertEqual(alts[LOCALES[other]['hreflang']],
                                     G.C.SITE['base_url'] + route(other, f"/{slug}/"))
                self.assertIn('x-default', alts)
                # Shared nav links to all four evergreen pages.
                for other in expected_slugs:
                    self.assertIn(f'href="{route(lang, f"/{other}/")}"', document)

    def test_evergreen_excluded_from_draft_preview(self):
        output = self.build(preview=True)
        for slug in G.EV.PAGES:
            self.assertFalse((output / slug / 'index.html').exists())

    def test_draft_preview_is_all_noindex_with_empty_sitemap(self):
        output = self.build(True)
        self.assertNotIn('<loc>', (output / 'sitemap.xml').read_text())
        for path in output.rglob('index.html'):
            document = path.read_text()
            self.assertIn('content="noindex,follow"', document)
            self.assertNotIn('application/ld+json', document)
        for lang in ('tr', 'yue', 'ko'):
            c = self.collection[lang][0]
            document = (output / G.chapter_path(c).strip('/') / 'index.html').read_text()
            self.assertIn(c['html'], document)
            self.assertIn(LOCALES[lang]['draft_notice'], document)

    def test_languages_and_canonical(self):
        output = self.build()
        for lang, t in LOCALES.items():
            document = (output / route(lang).strip('/') / 'index.html').read_text()
            tags = Tags(document)
            self.assertEqual(tags.attrs('html')[0]['lang'], t['lang'])
            canonical = [a['href'] for a in tags.attrs('link') if a.get('rel') == 'canonical']
            self.assertEqual(canonical, [G.C.SITE['base_url'] + route(lang)])
            self.assertIn('data-ai-disclosure="true"', document)
            self.assertIn('apprank studio', document)

    def test_all_local_links_exist_in_both_modes(self):
        for preview in (False, True):
            output = self.build(preview)
            for path in output.rglob('index.html'):
                for a in Tags(path.read_text()).attrs('a'):
                    href = a.get('href', '')
                    if href.startswith('/') and href.endswith(('.xml', '.txt')):
                        self.assertTrue((output / href.strip('/')).exists(), (path, href))
                    elif href.startswith('/'):
                        self.assertTrue((output / href.strip('/') / 'index.html').exists(), (path, href))

    def test_chapter_switch_preserves_chapter_when_available(self):
        slug = self.collection['en'][0]['slug']
        with patch.object(G.C, 'PREVIEW_DRAFTS', True):
            switches = G.chapter_switches(self.collection, slug)
            for lang in LOCALES:
                self.assertEqual(switches[lang], route(lang, f'/chapters/{slug}/'))
        with patch.object(G.C, 'PREVIEW_DRAFTS', False):
            self.assertEqual(G.chapter_switches(self.collection, slug)['tr'], '/tr/')

    def test_reciprocal_alternates_after_independent_approval(self):
        # In-memory fixture only: no source, status, review-log, or git is modified.
        collection = copy.deepcopy(self.collection)
        collection['tr'][0]['approved'] = True
        collection['yue'][0]['approved'] = True
        output = self.build(collection=collection)
        slug = collection['en'][0]['slug']
        suffix = f'/chapters/{slug}/'
        expected = G.page_alternates(collection, suffix)
        for lang in ('en', 'tr'):
            document = (output / route(lang, suffix).strip('/') / 'index.html').read_text()
            alternates = {a['hreflang']: a['href'] for a in Tags(document).attrs('link') if a.get('rel') == 'alternate' and 'hreflang' in a}
            self.assertEqual(alternates['x-default'], G.C.SITE['base_url'] + suffix)
            for candidate, path in expected.items():
                if candidate in G.C.SUMMARY_LANGS:
                    continue
                self.assertEqual(alternates[LOCALES[candidate]['hreflang']], G.C.SITE['base_url'] + path)
            self.assertNotIn('ko', alternates)
            self.assertNotIn(LOCALES['yue']['hreflang'], alternates)
            schema = json.loads(document.split('<script type="application/ld+json">')[1].split('</script>')[0])
            self.assertEqual(schema[0]['inLanguage'], LOCALES[lang]['lang'])

    def test_json_quoted_front_matter(self):
        meta, body = G.parse_front_matter('---\nreview_notes: "Changed \\"word\\" and pacing."\n---\nBody')
        self.assertEqual(meta['review_notes'], 'Changed "word" and pacing.')
        self.assertEqual(body, 'Body')

    def test_preview_cannot_overwrite_production(self):
        with patch.object(G.C, 'PREVIEW_DRAFTS', True), patch.object(G.C, 'OUTPUT_DIR', 'site'):
            with self.assertRaises(ValueError):
                G.main()

    def test_publish_gate_in_isolated_copy_without_git(self):
        # Only copy explicitly required files. In particular, NEVER copy .git or origin.
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for folder in ('tools', 'src', 'content/chapters', 'content/translations/tr', 'content/editorial', 'content/books'):
                (root / folder).mkdir(parents=True, exist_ok=True)
            for name in ('generate.py', 'config.py', 'locales.py', 'evergreen.py', 'glossary.py', 'acts.py', 'extras.py',
             'books.py', 'bookcopy.py', 'multibook.py'):
                shutil.copyfile(G.ROOT / 'src' / name, root / 'src' / name)
            script = root / 'tools/publish-chapter.sh'
            shutil.copyfile(G.ROOT / 'tools/publish-chapter.sh', script)
            source = self.collection['en'][0]['path']
            original = root / 'content/chapters' / source.name
            translation = root / 'content/translations/tr' / source.name
            shutil.copyfile(source, original)
            shutil.copyfile(self.collection['tr'][0]['path'], translation)
            fixture = translation.read_text()
            fixture = re.sub(r'(?m)^status:.*$', 'status: ai-draft', fixture, count=1)
            fixture = re.sub(r'(?m)^source_sha256:.*$', 'source_sha256: ' + G.source_digest(original), fixture, count=1)
            translation.write_text(fixture)
            log = root / 'content/editorial/review-log.md'
            log.write_text('# TEST FIXTURE ONLY\n')
            env = {**os.environ, 'REVIEWER': 'TEST FIXTURE ONLY',
                   'REVIEW_NOTES': 'Fixture-only edit to wording and pacing, never a real approval.'}
            command = ['bash', str(script), '01', '--lang', 'tr', '--local-only']
            result = subprocess.run(command + ['--dry-run'], env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(G.read_doc(translation)[0]['status'], 'ai-draft')
            result = subprocess.run(command, env={**env, 'REVIEW_NOTES': 'approved'}, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(G.read_doc(translation)[0]['status'], 'ai-draft')
            result = subprocess.run(command, env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            meta = G.read_doc(translation)[0]
            self.assertTrue(G.translation_approved(meta, G.read_doc(original)[0], G.source_digest(original)))
            self.assertIn('[tr]', log.read_text())
            self.assertFalse((root / '.git').exists())

    def test_published_edition_is_classical_fusion(self):
        chapters = G.load_chapters('en')
        self.assertGreaterEqual(len(chapters), 12)
        fused = [c for c in chapters if int(c['num']) <= 3]
        self.assertTrue(all(c['approved'] for c in fused))
        self.assertTrue(all(G.read_doc(c['path'])[0].get('edition') == 'classical-fusion' for c in fused))
        # As of 2026-11-24 all twelve chapters are approved in English. Ch.10-12
        # were released by explicit user instruction and carry approval fields;
        # no ai-draft remains and no act-2 draft is silently treated as live.
        approved = [c for c in chapters if c['approved']]
        self.assertEqual(len(approved), len(chapters))
        self.assertEqual(sorted(int(c['num']) for c in approved),
                         list(range(1, len(chapters) + 1)))
        drafts = [c for c in chapters if not c['approved']]
        self.assertEqual(drafts, [])
        finale = [c for c in chapters if 10 <= int(c['num']) <= 12]
        self.assertEqual(len(finale), 3)
        self.assertTrue(all(c['approved'] for c in finale))
        for c in finale:
            meta = G.read_doc(c['path'])[0]
            self.assertEqual(meta['edition'], 'classical-fusion')
            self.assertEqual(meta['language'], 'en')
            self.assertEqual(meta['approval_basis'], 'user-release-request')
            self.assertEqual(meta['reviewer'], 'apprank studio')
            self.assertEqual(meta['review_date'], '2026-11-24')
            self.assertGreater(c['words'], 0)
        # Season two (chapters 13-20) added on 2026-11-25 under the same gate.
        season_two = [c for c in chapters if int(c['num']) >= 13]
        self.assertEqual(len(season_two), 8)
        for c in season_two:
            meta = G.read_doc(c['path'])[0]
            self.assertTrue(c['approved'])
            self.assertEqual(meta['edition'], 'classical-fusion')
            self.assertEqual(meta['language'], 'en')
            self.assertEqual(meta['approval_basis'], 'user-content-expansion')
            self.assertEqual(meta['review_date'], '2026-11-25')
            self.assertGreater(c['words'], 400)
        act2 = [c for c in chapters if 4 <= int(c['num']) <= 6]
        self.assertEqual(len(act2), 3)
        self.assertTrue(all(c['approved'] for c in act2))
        self.assertTrue(all(G.read_doc(c['path'])[0].get('approval_basis') == 'user-release-request'
                            for c in act2))
        continuation = [c for c in chapters if 7 <= int(c['num']) <= 9]
        self.assertEqual(len(continuation), 3)
        self.assertTrue(all(c['approved'] for c in continuation))
        self.assertTrue(all(G.read_doc(c['path'])[0].get('approval_basis') == 'user-release-request'
                            for c in continuation))
        # A scorched cloth and the archive token only exist in the fused edition.
        # Build into a temporary directory: CI does not contain the generated site/.
        output = self.build()
        first = (output / 'chapters/the-shop-on-cinder-lane/index.html').read_text()
        self.assertIn('scorched', first)
        self.assertNotIn('Nobody ever thanked him for the seam', first)
        # As of 2026-11-25 all twenty chapters are approved and published in
        # all four languages (season two added 13-20). Every post-fusion approval
        # is explicitly recorded as a user release request or a multilingual
        # completion without claiming sentence-level rewrites.
        for lang in ('tr', 'yue', 'ko'):
            chapters = G.load_chapters(lang)
            approved = [c for c in chapters if c['approved']]
            drafts = [c for c in chapters if not c['approved']]
            self.assertEqual(len(chapters), 20)
            self.assertEqual(len(approved), 20)
            self.assertEqual(sorted(int(c['num']) for c in approved), list(range(1, 21)))
            self.assertEqual(drafts, [])
            for c in approved:
                meta = G.read_doc(c['path'])[0]
                self.assertEqual(meta.get('edition'), 'classical-fusion')
                self.assertTrue(meta.get('reviewer', '').strip())
                self.assertEqual(meta.get('language'), lang)
                # Chapters released on 2026-11-24 carry an explicit basis.
                if int(c['num']) in (4, 5, 6, 10, 11, 12):
                    self.assertEqual(meta.get('approval_basis'), 'user-release-request')
                src = G.ROOT / 'content/chapters' / c['path'].name
                self.assertTrue(G.translation_approved(
                    meta, G.read_doc(src)[0], G.source_digest(src)))

    def test_revision_requires_local_draft_preview(self):
        with patch.object(G.C, 'REVISION_SET', 'classical-fusion'), patch.object(G.C, 'PREVIEW_DRAFTS', False):
            with self.assertRaises(ValueError):
                G.load_chapters('en')
            with self.assertRaises(ValueError):
                G.main()

    def test_revision_rejects_invalid_names(self):
        for name in ('../chapters', '/tmp', 'unknown-revision'):
            with patch.object(G.C, 'REVISION_SET', name), patch.object(G.C, 'PREVIEW_DRAFTS', True):
                with self.assertRaises(ValueError):
                    G.revision_root()

    def test_revision_does_not_reuse_old_translations(self):
        with patch.object(G.C, 'REVISION_SET', 'classical-fusion'), patch.object(G.C, 'PREVIEW_DRAFTS', True):
            chapters = G.load_chapters('en')
            self.assertEqual(len(chapters), 3)
            for c in chapters:
                self.assertFalse(c['approved'])
                self.assertEqual(c['status'], 'ai-draft')
                self.assertGreater(c['words'], 700)
            for lang in ('tr', 'yue', 'ko'):
                self.assertEqual(G.load_chapters(lang), [])

    def test_revision_preview_isolated_and_disclosed(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            with patch.object(G.C, 'REVISION_SET', 'classical-fusion'), patch.object(G.C, 'PREVIEW_DRAFTS', True), patch.object(G.C, 'OUTPUT_DIR', str(output)):
                G.main()
            self.assertEqual(len(list(output.rglob('index.html'))), 6)
            self.assertNotIn('<loc>', (output / 'sitemap.xml').read_text())
            self.assertFalse((output / 'tr').exists())
            self.assertTrue((output / 'revision-notes/index.html').exists())
            for path in output.rglob('index.html'):
                document = path.read_text()
                self.assertIn('content="noindex,follow"', document)
                self.assertIn('not been human-reviewed', document)
                self.assertNotIn('application/ld+json', document)
                self.assertNotIn('hreflang=', document)
                for a in Tags(document).attrs('a'):
                    href = a.get('href', '')
                    if href.startswith('/') and href.endswith(('.xml', '.txt')):
                        self.assertTrue((output / href.strip('/')).exists(), (path, href))
                    elif href.startswith('/'):
                        self.assertTrue((output / href.strip('/') / 'index.html').exists(), (path, href))

    def test_revision_cannot_replace_original_preview(self):
        with patch.object(G.C, 'REVISION_SET', 'classical-fusion'), patch.object(G.C, 'PREVIEW_DRAFTS', True), patch.object(G.C, 'OUTPUT_DIR', 'preview-site'):
            with self.assertRaises(ValueError):
                G.main()


if __name__ == '__main__':
    unittest.main()
