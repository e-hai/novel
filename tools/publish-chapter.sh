#!/usr/bin/env bash
# ============================================================
# 人工审校发布闸门：把一个 ai-draft 章节升级为 approved 并上线
#
# 这是合规的核心关口 —— 脚本强制你：
#   1. 输入审核人署名
#   2. 写下"你对本章做了什么实质修改"（不能空、不能敷衍）
# 然后脚本才：改状态 → 写审校日志 → 提交 → 推送 → 触发部署。
#
# 用法:
#   ./tools/publish-chapter.sh 04                    # 发布第4章（自动匹配 04-*.md）
#   ./tools/publish-chapter.sh 04-the-woman-who-kept-receipts   # 精确 slug
#   ./tools/publish-chapter.sh 04 --dry-run          # 预览不改
#   ./tools/publish-chapter.sh 01 --lang tr --dry-run # 土耳其语独立审校
#   --lang: en / tr / yue / ko；--local-only: 不提交、不推送
#
# 环境:
#   REVIEWER       审核人署名（不设则交互式询问，默认 apprank studio）
#   REVIEW_NOTES   实质修改说明（不设则交互式询问）
# ============================================================
set -euo pipefail

cd "$(dirname "$0")/.."   # 仓库根目录

if [[ $# -lt 1 || "$1" == "-h" || "$1" == "--help" ]]; then
  sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'
  exit 0
fi

KEY="$1"; shift
DRY=0
LANGUAGE=en
LOCAL_ONLY=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY=1; shift ;;
    --local-only) LOCAL_ONLY=1; shift ;;
    --lang)
      [[ $# -ge 2 ]] || { echo "--lang 需要语言代码" >&2; exit 1; }
      LANGUAGE="$2"; shift 2 ;;
    *) echo "未知参数: $1" >&2; exit 1 ;;
  esac
done
[[ "$LANGUAGE" =~ ^(en|tr|yue|ko)$ ]] || { echo "不支持的语言" >&2; exit 1; }
[[ "$KEY" =~ ^[a-z0-9-]+$ ]] || { echo "无效章节标识" >&2; exit 1; }
DIR=content/chapters
[[ "$LANGUAGE" == en ]] || DIR="content/translations/$LANGUAGE"

# ---------- 定位章节文件 ----------
shopt -s nullglob
matches=("$DIR"/${KEY}*.md)
if [[ ${#matches[@]} -eq 0 ]]; then
  echo "✗ 找不到匹配 '${KEY}' 的章节文件（在 ${DIR}/ 下）" >&2
  exit 1
fi
if [[ ${#matches[@]} -gt 1 ]]; then
  echo "✗ 匹配到多个文件，请用更精确的 slug：" >&2
  printf '  %s\n' "${matches[@]}" >&2
  exit 1
fi
CH="${matches[0]}"
echo "→ 章节文件: ${CH}"

# ---------- 校验状态 ----------
status="$(grep -m1 '^status:' "$CH" | sed 's/^status:[[:space:]]*//')"
if [[ "$status" != "ai-draft" ]]; then
  echo "✗ 本章状态是 '${status}'，不是 ai-draft；只有草稿才能走发布闸门。" >&2
  exit 1
fi
echo "  当前状态: ${status} ✓"

# 译文必须基于当前已批准原文；原文批准不能代替译文审核。
if [[ "$LANGUAGE" != en ]]; then
  python3 - "$CH" "$LANGUAGE" <<'PY'
import sys
from pathlib import Path
sys.path.insert(0, 'src')
from generate import read_doc, source_digest
p = Path(sys.argv[1])
meta = read_doc(p)[0]
source = Path('content/chapters') / p.name
if not source.exists() or read_doc(source)[0].get('status') != 'approved':
    raise SystemExit('原文章节不存在或尚未获批准，不能发布译文。')
if meta.get('language') != sys.argv[2] or meta.get('source_sha256') != source_digest(source):
    raise SystemExit('译文语言不匹配或原文已改变，请更新翻译并重新审校。')
PY
fi

# ---------- 提取标题/章号 ----------
title="$(grep -m1 '^title:' "$CH" | sed 's/^title:[[:space:]]*//; s/^"//; s/"$//')"
num="$(grep -m1 '^chapter:' "$CH" | sed 's/^chapter:[[:space:]]*//')"

# ---------- 强制人工输入 ----------
REVIEWER="${REVIEWER:-}"
NOTES="${REVIEW_NOTES:-}"
if [[ -z "$REVIEWER" ]]; then
  read -r -p "审核人署名 [apprank studio]: " REVIEWER
  REVIEWER="${REVIEWER:-apprank studio}"
fi
if [[ -z "$NOTES" ]]; then
  echo "请写下你对本章做的**实质修改**（读过之后到底改了什么）。"
  echo "不要写'已审核'/'通过'这类空话——那正是被政策盯上的痕迹。"
  read -r -p "实质修改说明: " NOTES
fi

# 校验说明不是敷衍：剔除常见空话词后仍需有足够有效内容
python3 - "$NOTES" <<'PY'
import sys, re
notes = sys.argv[1]
if len(notes) < 12:
    print(f"✗ 修改说明太短（{len(notes)} 字符）。请具体说明你改了什么，至少 12 个字符。", file=sys.stderr)
    sys.exit(1)
# 去掉常见敷衍语后，看还剩多少实质内容
filler = re.compile(
    r'(lgtm|looks good|approved|已审核|审核通过|通过|没问题|可以|okay|ok|good|fine|'
    r'great|nice|perfect|done|checked|reviewed|ship it|sgtm)',
    re.I)
stripped = filler.sub('', notes)
stripped = re.sub(r'[\s。.!！，,、；;：:]+', '', stripped)
if len(stripped) < 8:
    print("✗ 这看起来是空话。请写你具体动了哪些句子、情节或措辞——记录会公开写进 review-log。", file=sys.stderr)
    sys.exit(1)
PY

DATE="$(date +%F)"

echo ""
echo "════ 发布预览 ════"
echo "  语言:      ${LANGUAGE}"
echo "  章节:      Ch.${num} — ${title}"
echo "  审核人:    ${REVIEWER}"
echo "  日期:      ${DATE}"
echo "  实质修改:  ${NOTES}"
echo ""

if [[ $DRY -eq 1 ]]; then
  echo "[dry-run] 未改动任何文件。"
  exit 0
fi

# ---------- 改写 front matter 状态 ----------
python3 - "$CH" "$LANGUAGE" "$REVIEWER" "$DATE" "$NOTES" <<'PY'
import sys, re, json
p, language, reviewer, date, notes = sys.argv[1:6]
s = open(p, encoding='utf-8').read()
s2 = re.sub(r'(?m)^status:[ \t]*ai-draft[ \t]*$', 'status: approved', s, count=1)
assert s2 != s, 'status 改写失败'
if language != 'en':
    # Keep a translation-specific review record in front matter as well as the log.
    header, body = s2.split('\n---', 1)
    for key, value in [('reviewer', reviewer), ('review_date', date), ('review_notes', notes)]:
        header = re.sub(r'(?m)^' + key + r':.*\n?', '', header)
        header += '\n' + key + ': ' + json.dumps(value, ensure_ascii=False)
    s2 = header + '\n---' + body
open(p, 'w', encoding='utf-8').write(s2)
PY

# ---------- 追加审校日志条目 ----------
python3 - "$num" "$title" "$REVIEWER" "$DATE" "$NOTES" "$LANGUAGE" <<'PY'
import sys
num, title, reviewer, date, notes, language = sys.argv[1:7]
p = 'content/editorial/review-log.md'
s = open(p, encoding='utf-8').read()
entry = (
    f'\n## Ch.{num} [{language}] — "{title}"\n\n'
    f'- **Status:** `approved`\n'
    f'- **Reviewer:** {reviewer}\n'
    f'- **Date:** {date}\n'
    f'- **Substantive changes:** {notes}\n'
    f'- **Approved to publish:** ☑ Yes — approved by {reviewer}, {date}\n'
)
# 插到 "Note to the human editor" 之前
marker = '\n---\n\n## Note to the human editor'
if marker in s:
    s = s.replace(marker, entry + marker, 1)
else:
    s = s.rstrip() + '\n' + entry
open(p, 'w', encoding='utf-8').write(s)
PY

echo "  ✓ front matter 状态 → approved"
echo "  ✓ 审校日志已追加"

# ---------- 提交并推送 ----------
if [[ $LOCAL_ONLY -eq 1 ]]; then
  echo "[local-only] 仅更新本地状态和真实审校记录；未提交、未推送。"
  exit 0
fi
git add "$CH" content/editorial/review-log.md
git -c user.name="WorkBuddy" -c user.email="workbuddy@local" \
  commit -q -m "Publish Ch.${num} [${LANGUAGE}]: ${title} (human review by ${REVIEWER})"
echo "  ✓ 已提交"

if git remote get-url origin >/dev/null 2>&1; then
  git push origin main 2>&1 | tail -2
  echo "  ✓ 已推送，workflow 将自动部署"
else
  echo "  ℹ 无 origin，未推送（本地提交完成）"
fi

echo ""
echo "════ 完成：Ch.${num} 已发布 ════"
