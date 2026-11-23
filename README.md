# Cinder Lane — 精品科幻小说站

《The Memory Repairman》：一个近未来科幻短篇，AI 起草、人工终审的精工试水站。

这是路线 A 的副站。和全自动的应用排行主站不同，这个站是**半自动**的：
批量 AI 生成铺站会踩 Google 的 scaled content abuse 红线，所以这里走"少量精工 + 人工关口"的路——宁可 3 篇精，不要 100 篇水。

## 合规设计（不可省的三道关口）

1. **发布门槛**：章节 front matter 里 `status: approved` 才会被发布；`ai-draft` 不发布，且其公开路径会自动生成 noindex 墓碑页（防止旧部署残留被收录）。
2. **人工审校记录**：`content/editorial/review-log.md` 记录每章的人工重写与签字。未签字 = 不发布。发布脚本会强制填写"实质修改说明"并写入此文件。
3. **每页 AI 披露**：所有页面底部显示"AI 辅助起草 + 人工编辑"声明，不伪造纯人类作者、不伪造头像履历。

作者署名由环境变量 `SITE_AUTHOR` 提供（当前 `apprank studio`，见 GitHub Variable）。生产域名 `https://novel-9wi.pages.dev`（`novel.pages.dev` 已被外部占用，故带后缀）。

## 本地运行

```bash
python3 src/generate.py                    # 正式模式：只发布 approved 章节
PREVIEW_DRAFTS=1 python3 src/generate.py   # 预览模式：显示草稿（带醒目草稿横幅 + noindex）
```

正式产物在 `site/`；草稿预览产物在 `preview-site/`，两者隔离。

## 每日一章：AI 起草 + 人工终审（推荐流程）

内容扩展走"**我批量备草稿 → 你每天读、改、签字发布**"的节奏。**绝不定时自动发布**——那是 scaled content abuse，会毁掉站。护城河是每章真实的人工投入。

- `content/outline-act2.md` 是第 4–12 章的故事骨架；草稿写在 `content/chapters/`，front matter 标 `status: ai-draft`（默认不发布）。
- 你每天挑一章：读 → 按 `world-bible.md` 核对 → 做**实质性**改写（不是同义词替换）→ 签字发布。

**发布一条命令搞定**（脚本会强制你填实质修改说明、写进 review-log、改状态、提交、推送、触发部署）：

```bash
./tools/publish-chapter.sh 04            # 发布第4章，交互式填审核人和修改说明
./tools/publish-chapter.sh 04 --dry-run  # 先预览，不改任何东西
# 也可非交互：REVIEWER="apprank studio" REVIEW_NOTES="具体改了什么" ./tools/publish-chapter.sh 04
```

脚本闸门：草稿状态校验、修改说明最短长度、拒绝"已审核/LGTM"类空话。因为说明会公开写进 GitHub 上的 review-log，这道关口才真正有效——技术只是提醒，诚实靠人。

## 部署（Cloudflare Pages）

首次部署需配置（与主站共用 Cloudflare 账号，但这是独立项目）：

1. GitHub 仓库 Settings → Secrets and variables → Actions 添加：
   - Secret `CLOUDFLARE_API_TOKEN`（Edit Cloudflare Workers 模板）
   - Secret `CLOUDFLARE_ACCOUNT_ID`
   - Variable `CF_PAGES_PROJECT` = `novel`（默认）
   - Variable `SITE_AUTHOR` = `apprank studio`
   - Variable `PREVIEW_DRAFTS` = 留空（正式）/ `1`（临时预览草稿，看完删掉）
   - Variable `SITE_BASE_URL` = `https://novel-9wi.pages.dev`（**必须与实际 pages.dev 域名一致**；可用 `ai-first/tools/setup-site.sh novel` 自动探测写入）
   - 可选 Variable `SITE_CONTACT`（联系邮箱）
2. workflow 用 `cloudflare/wrangler-action@v4`，会自动建 Pages 项目并部署。
3. 换独立域名改 `SITE_BASE_URL` 即可，代码不动。

注意：`PREVIEW_DRAFTS=1` 时草稿页会带 `noindex`，即便部署了也不会被搜索引擎收录——这是有意的保护。

## 目录结构

```
content/
  world-bible.md              世界观设定
  outline.md                  第一幕三章大纲
  outline-act2.md             第二幕 4–12 章大纲（草稿计划）
  chapters/*.md               章节正文（front matter 含 status/words）
  editorial/
    ai-disclosure.md          AI 披露（每页展示）
    review-log.md             人工审校记录（发布关口）
src/
  config.py                   站点/作品/作者配置
  generate.py                 静态站生成器（零第三方依赖，含草稿墓碑）
tools/
  publish-chapter.sh          人工审校发布闸门（强制修改说明+签字）
```

## 当前状态（2026-11-23）

- 正式发布：第 1–9 章全部 `approved`。第 1–3 章为 classical-fusion 四语言；第 4–6 章为英文；第 7–9 章为四语言。GSC 已验证 `novel-9wi.pages.dev` 并提交 sitemap。
- 草稿待审：暂无章节草稿。第 10–12 章仍只有大纲。
- 2026-11-23 完成用户选择的任务 1 和 2：第 7–9 章已翻译为土耳其语、粤语、韩语并发布；第 4–6 章已按用户授权审核发布。未声称逐句人工改写，审核依据均如实写入 `review-log.md`。
- 扩量铁律：每篇都有人工重写记录 + 披露，0 篇未审校直发；宁可慢，不要被判 scaled content abuse。
