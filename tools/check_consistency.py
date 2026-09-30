"""文档一致性检查（push 前跑一次）

检查项：
  1. PROBLEMS.md / README.md 中每个题目的链接文件是否存在
  2. 同一题在两个文档里的状态是否一致
  3. 状态 ✅ 的题目，其文件里的「解法 / 时间复杂度 / 空间复杂度」是否已填写
  4. 状态 ⬜ 的题目，是否其实已经写完（写了但没同步）
  5. PROBLEMS.md 末尾统计表的数字是否与实际一致
  6. 某题型全部完成时，文件夹内是否有 notes.md
  7. 文本文件中是否存在损坏字符 U+FFFD
  8. 所有 .py 文件是否能通过语法编译

用法：python tools/check_consistency.py
退出码：0 = 全部通过；1 = 存在 ERROR
"""

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ROW = re.compile(r"^\|\s*(\d+)\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]+?)\s*\|\s*(\S+)\s*\|\s*$")
FOLDER = re.compile(r"`(leetcode/[^`]*?)/?`")
EMPTY_LABEL = re.compile(r"#\s*(解法|时间复杂度|空间复杂度)\s*[：:]\s*$", re.M)

errors, warnings = [], []


def parse(path):
    """解析文档中的题目表格 -> {题号: {...}}"""
    rows, section = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            m = FOLDER.search(line)
            if m:
                section = m.group(1)
            continue
        m = ROW.match(line)
        if m and section:
            num, title, link, diff, status = m.groups()
            rows[int(num)] = dict(title=title, link=link, diff=diff,
                                  status=status, section=section)
    return rows


problems = parse(ROOT / "PROBLEMS.md")
readme = parse(ROOT / "README.md")

# --- 1 & 2：链接存在 + 两文档状态一致 ---
for num, info in sorted(problems.items()):
    if not (ROOT / info["link"]).exists():
        errors.append(f"[链接失效] #{num} {info['link']} 不存在")
    other = readme.get(num)
    if other is None:
        warnings.append(f"[README 缺行] #{num} {info['title']} 未出现在 README.md")
    elif other["status"] != info["status"]:
        errors.append(f"[状态不一致] #{num} PROBLEMS={info['status']} README={other['status']}")

# --- 3 & 4：状态与文件实际内容是否吻合 ---
for num, info in sorted(problems.items()):
    py = ROOT / info["link"]
    if not py.exists():
        continue
    text = py.read_text(encoding="utf-8")
    has_empty = bool(EMPTY_LABEL.search(text))
    if info["status"] == "✅" and has_empty:
        errors.append(f"[未填完] #{num} 标记为 ✅ 但文件里仍有空的 解法/复杂度 注释")
    if info["status"] == "⬜" and not has_empty:
        warnings.append(f"[可能漏同步] #{num} 标记为 ⬜ 但文件里已无空注释")


# --- 5：统计表数字 ---
def parse_stats():
    stats, in_table = {}, False
    for line in (ROOT / "PROBLEMS.md").read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("| 题型 |"):
            in_table = True
            continue
        if in_table:
            if not line.strip().startswith("|"):
                break
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 3 and cells[0] and not set(cells[0]) <= {"-", " "}:
                stats[cells[0].replace("*", "")] = (cells[1].replace("*", ""), cells[2].replace("*", ""))
    return stats


by_section = defaultdict(Counter)
for info in problems.values():
    by_section[info["section"]][info["status"]] += 1

SECTION_LABEL = {
    "leetcode/array_hashing": "数组 & 哈希表",
    "leetcode/two_pointers": "双指针",
    "leetcode/sliding_window": "滑动窗口",
    "leetcode/stack": "栈",
    "leetcode/linked_list": "链表",
}

stats = parse_stats()
total_done = total_todo = 0
for folder, label in SECTION_LABEL.items():
    c = by_section.get(folder, Counter())
    done, todo = c["✅"], c["⬜"]
    total_done += done
    total_todo += todo
    if label in stats:
        got_done, got_todo = stats[label]
        if (got_done, got_todo) != (str(done), str(todo)):
            errors.append(f"[统计不符] {label}: 文档写 {got_done}/{got_todo}，实际 {done}/{todo}")
    else:
        warnings.append(f"[统计缺行] {label} 未出现在统计表中")

if "LeetCode 合计" in stats:
    got_done, got_todo = stats["LeetCode 合计"]
    if (got_done, got_todo) != (str(total_done), str(total_todo)):
        errors.append(f"[统计不符] LeetCode 合计: 文档写 {got_done}/{got_todo}，实际 {total_done}/{total_todo}")

# --- 6：章节全部完成 -> 必须有 notes.md ---
for folder, c in by_section.items():
    if c["⬜"] == 0 and c["✅"] > 0 and not (ROOT / folder / "notes.md").exists():
        errors.append(f"[缺章节笔记] {folder} 已全部完成，但没有 notes.md")

# --- 7：文本文件中是否存在损坏字符 U+FFFD（编辑器/工具误操作会导致 emoji 变乱码）---
SKIP_DIRS = {".git", ".venv", "__pycache__"}
for p in sorted(ROOT.rglob("*")):
    if not p.is_file() or any(part in SKIP_DIRS for part in p.parts):
        continue
    if p.suffix not in {".md", ".py"}:
        continue
    try:
        text = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"[编码错误] {p.relative_to(ROOT)} 不是合法 UTF-8")
        continue
    if "\ufffd" in text:
        errors.append(f"[损坏字符] {p.relative_to(ROOT)} 含 U+FFFD 替换字符")

# --- 8：所有 .py 文件语法必须可编译（不写 .pyc，避免产生副产物）---
for p in sorted(ROOT.rglob("*.py")):
    if any(part in SKIP_DIRS for part in p.parts):
        continue
    try:
        compile(p.read_text(encoding="utf-8"), str(p), "exec")
    except SyntaxError as e:
        errors.append(f"[语法错误] {p.relative_to(ROOT)}:{e.lineno}  {e.msg}")

# --- 输出 ---
print(f"题目总数: {len(problems)}   已完成 {total_done}   待完成 {total_todo}\n")
for w in warnings:
    print("  WARN ", w)
for e in errors:
    print("  ERROR", e)
if not warnings and not errors:
    print("  ✅ 文档与文件状态完全一致")
sys.exit(1 if errors else 0)
