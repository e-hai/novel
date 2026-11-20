# Cinder Lane — 精品科幻小说站

《The Memory Repairman》：一个近未来科幻短篇，AI 起草、人工终审的精工试水站。

这是路线 A 的副站。和全自动的应用排行主站不同，这个站是**半自动**的：
批量 AI 生成铺站会踩 Google 的 scaled content abuse 红线，所以这里走"少量精工 + 人工关口"的路——宁可 3 篇精，不要 100 篇水。

## 合规设计（不可省的三道关口）

1. **发布门槛**：章节 front matter 里 `status: approved` 才会被发布。当前三章都是 `ai-draft`，默认不发布。
2. **人工审校记录**：`content/editorial/review-log.md` 记录每章的人工重写与签字。未签字 = 不发布。
3. **每页 AI 披露**：所有页面底部显示"AI 辅助起草 + 人工编辑"声明，不伪造纯人类作者、不伪造头像履历。

作者署名由环境变量 `SITE_AUTHOR` 提供（默认 `C. Vale`），**请人类编辑改成自己的真实署名**。

## 本地运行

```bash
python3 src/generate.py                    # 正式模式：只发布 approved 章节
PREVIEW_DRAFTS=1 python3 src/generate.py   # 预览模式：显示草稿（带醒目草稿横幅 + noindex）
```

产物在 `site/`。

## 章节审稿流程

1. 读 `content/chapters/*.md`（这些是 AI 草稿，不是成品）。
2. 朗读一遍，改掉不像你语气的句子；按 `content/world-bible.md` 核对一致性。
3. 做**实质性**改写——不是同义词替换（obfuscation 是明列违规）。
4. 在 `content/editorial/review-log.md` 记录你实际改了什么、签字、勾选批准。
5. 把章节 front matter 的 `status: ai-draft` 改成 `status: approved`。
6. push 到 main，workflow 自动重建部署。

## 部署（Cloudflare Pages）

首次部署需配置（与主站共用 Cloudflare 账号，但这是独立项目）：

1. GitHub 仓库 Settings → Secrets and variables → Actions 添加：
   - Secret `CLOUDFLARE_API_TOKEN`（Edit Cloudflare Workers 模板）
   - Secret `CLOUDFLARE_ACCOUNT_ID`
   - Variable `CF_PAGES_PROJECT` = `novel`（默认）
   - Variable `SITE_AUTHOR` = 你的真实署名（默认 `C. Vale`）
   - Variable `PREVIEW_DRAFTS` = 留空（正式）/ `1`（临时预览草稿，看完删掉）
   - 可选 Variable `SITE_BASE_URL`（换独立域名时改）、`SITE_CONTACT`（联系邮箱）
2. workflow 用 `cloudflare/wrangler-action@v4`，会自动建 Pages 项目并部署。
3. 默认域名 `https://novel.pages.dev`；换独立域名改 `SITE_BASE_URL` 即可，代码不动。

注意：`PREVIEW_DRAFTS=1` 时草稿页会带 `noindex`，即便部署了也不会被搜索引擎收录——这是有意的保护。

## 目录结构

```
content/
  world-bible.md              世界观设定
  outline.md                  三章大纲
  chapters/*.md               章节正文（front matter 含 status/words）
  editorial/
    ai-disclosure.md          AI 披露（每页展示）
    review-log.md             人工审校记录（发布关口）
src/
  config.py                   站点/作品/作者配置
  generate.py                 静态站生成器（零第三方依赖）
```

## 后续

- 人工审校三章 → 改 `status: approved` → 正式发布。
- 若要扩量，坚持"每篇都有人工重写记录 + 披露，0 篇未审校直发"的验收标准。
- 上线后到 GSC / Bing 验证 `novel.pages.dev` 并提交 sitemap。
