# 仓库规范（Algorithm Journey）

本文件是本仓库的**唯一规范来源**。任何改动（尤其是新增/完成题目）都必须遵守以下约定。

## 1. 目录结构

```
leetcode/<题型>/<题号>_<snake_case题目名>.py   # LeetCode 题解，按题型分类
sorting/*.py                                  # 经典排序算法
sorting/problems/*.py                         # 排序思想的延伸应用
notes/                                        # 专题笔记
PROBLEMS.md                                   # 📋 题目清单索引（权威进度来源）
README.md                                     # 项目说明 + 目录结构 + 进度总览
```

题型文件夹使用小写下划线命名：`array_hashing` / `two_pointers` / `sliding_window` / `stack`。

## 2. 题目文件命名

- 格式：`<题号>_<snake_case题目名>.py`，例如 `84_largest_rectangle_in_histogram.py`。
- 题号前缀不可省略，便于按号检索。

## 3. 题目文件模板

- 使用 `class Solution(object):`，方法签名保留 LeetCode 的 `:type / :rtype` docstring。
- 非 `Solution` 类的题目（如 155 Min Stack）按 LeetCode 原样保留类名与方法。
- **新建时只写骨架，不写答案**：保留
  ```
  # 解法：
  # 时间复杂度：
  # 空间复杂度：
  ```
  三行空注释，底部 `print(...)` 示例整行注释掉供自测。
- 完成后在文件内保留从**暴力 → 优化 → 最优**的演进过程（早期版本以注释形式留档）。
- 中文注释，风格与现有文件保持一致。

## 4. 【核心规则】状态自动同步

**触发条件**：某题文件由空骨架变为写入完整解法（docstring 下的「解法/时间复杂度/空间复杂度」已填写，或用户明确表示写完），即视为**该题完成**。

**自动执行**（无需用户再次提醒）：

1. `PROBLEMS.md` 中该题所在行：状态 `⬜` → `✅`。
2. `README.md` 中该题所在行：状态 `⬜` → `✅`。
3. 更新 `PROBLEMS.md` 末尾「🗂️ 统计」表中对应题型的 `已完成` / `待完成` 数字，以及 `LeetCode 合计` 行。
4. 若某题型此前不存在于两个文件，则先补建对应小节/表格再同步。

**新建题目时**：在 `PROBLEMS.md` 与 `README.md` 的对应题型表格中新增一行，状态默认 `⬜`，并同步统计数字。

## 5. Git 操作约定

- 用户说「**git 保存**」= **只做本地提交（`git add` + `git commit`），不要 push**。
- 只有用户明确说「**push**」「上传」「推到 GitHub」时才执行 `git push`。
- 提交信息用中文或英文皆可，格式建议 `<type>: <简述>`（如 `feat(stack): 完成第 155 题`）。
- 远程走 **SSH over 443**（详见 README「🔐 Git 推送(SSH over 443)」），一般无需开启 VPN。

## 6. 提交前自检

- [ ] 文件命名符合 `题号_snake_case.py`
- [ ] 无答案残留于未完成的骨架文件
- [ ] `PROBLEMS.md` 与 `README.md` 的题号、链接、状态、统计数字三者一致
