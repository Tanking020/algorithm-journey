# Algorithm Journey

> LeetCode solutions & classic sorting algorithms, with brute-force → optimal evolution and detailed annotations.

个人算法学习记录。每道题的解法文件都保留了从**暴力解 → 逐步优化 → 最优解**的完整演进过程,
早期方案以注释形式留在同一个文件中,方便日后回顾思路变化,而不只是看一个"标准答案"。

---

## 📁 目录结构

```
algorithm-journey/
├── leetcode/               # LeetCode 题解(按题型分类)
│   ├── array_hashing/      # 数组 & 哈希表(含 notes.md 章节笔记)
│   ├── two_pointers/       # 双指针(含 notes.md)
│   ├── sliding_window/     # 滑动窗口(含 notes.md)
│   ├── stack/              # 栈(含 notes.md)
│   └── linked_list/        # 链表(含 notes.md)
├── sorting/                # 经典排序算法
│   └── problems/           # 排序思想的延伸应用(逆序对、小和、荷兰国旗)
├── notes/                  # 跨题型通用专题(与章节笔记区分)
├── tools/                  # 仓库工具(check_consistency.py 文档一致性检查)
├── PROBLEMS.md             # 📋 题目清单索引(题号 + 链接 + 状态)
└── README.md
```

---

## 🧩 LeetCode 进度

### 数组 & 哈希表 · `leetcode/array_hashing/`

| # | 题目 | 难度 | 状态 |
|---|---|---|---|
| 1 | [Two Sum](leetcode/array_hashing/1_two_sum.py) | Easy | ✅ |
| 49 | [Group Anagrams](leetcode/array_hashing/49_group_anagrams.py) | Medium | ✅ |
| 128 | [Longest Consecutive Sequence](leetcode/array_hashing/128_longest_consecutive_sequence.py) | Medium | ✅ |
| 242 | [Valid Anagram](leetcode/array_hashing/242_valid_anagram.py) | Easy | ✅ |
| 349 | [Intersection of Two Arrays](leetcode/array_hashing/349_intersection_of_two_arrays.py) | Easy | ✅ |
| 560 | [Subarray Sum Equals K](leetcode/array_hashing/560_subarray_sum_equals_k.py) | Medium | ✅ |

### 双指针 · `leetcode/two_pointers/`

| # | 题目 | 难度 | 状态 |
|---|---|---|---|
| 11 | [Container With Most Water](leetcode/two_pointers/11_container_with_most_water.py) | Medium | ✅ |
| 15 | [3Sum](leetcode/two_pointers/15_three_sum.py) | Medium | ✅ |
| 18 | [4Sum](leetcode/two_pointers/18_four_sum.py) | Medium | ✅ |
| 167 | [Two Sum II - Input Array Is Sorted](leetcode/two_pointers/167_two_sum_ii_input_array_is_sorted.py) | Medium | ✅ |

### 滑动窗口 · `leetcode/sliding_window/`

| # | 题目 | 难度 | 状态 |
|---|---|---|---|
| 3 | [Longest Substring Without Repeating Characters](leetcode/sliding_window/3_longest_substring_without_repeating_characters.py) | Medium | ✅ |
| 76 | [Minimum Window Substring](leetcode/sliding_window/76_minimum_window_substring.py) | Hard | ✅ |
| 209 | [Minimum Size Subarray Sum](leetcode/sliding_window/209_minimum_size_subarray_sum.py) | Medium | ✅ |
| 438 | [Find All Anagrams in a String](leetcode/sliding_window/438_find_all_anagrams_in_a_string.py) | Medium | ✅ |
| 567 | [Permutation in String](leetcode/sliding_window/567_permutation_in_string.py) | Medium | ✅ |

### 栈 · `leetcode/stack/`

| # | 题目 | 难度 | 状态 |
|---|---|---|---|
| 20 | [Valid Parentheses](leetcode/stack/20_valid_parentheses.py) | Easy | ✅ |
| 84 | [Largest Rectangle in Histogram](leetcode/stack/84_largest_rectangle_in_histogram.py) | Hard | ✅ |
| 155 | [Min Stack](leetcode/stack/155_min_stack.py) | Medium | ✅ |
| 739 | [Daily Temperatures](leetcode/stack/739_daily_temperatures.py) | Medium | ✅ |

### 链表 · `leetcode/linked_list/`

| # | 题目 | 难度 | 状态 |
|---|---|---|---|
| 2 | [Add Two Numbers](leetcode/linked_list/2_add_two_numbers.py) | Medium | ⬜ |
| 19 | [Remove Nth Node From End of List](leetcode/linked_list/19_remove_nth_node_from_end_of_list.py) | Medium | ⬜ |
| 21 | [Merge Two Sorted Lists](leetcode/linked_list/21_merge_two_sorted_lists.py) | Easy | ✅ |
| 141 | [Linked List Cycle](leetcode/linked_list/141_linked_list_cycle.py) | Easy | ✅ |
| 142 | [Linked List Cycle II](leetcode/linked_list/142_linked_list_cycle_ii.py) | Medium | ⬜ |
| 143 | [Reorder List](leetcode/linked_list/143_reorder_list.py) | Medium | ⬜ |
| 146 | [LRU Cache](leetcode/linked_list/146_lru_cache.py) | Medium | ⬜ |
| 206 | [Reverse Linked List](leetcode/linked_list/206_reverse_linked_list.py) | Easy | ✅ |
| 234 | [Palindrome Linked List](leetcode/linked_list/234_palindrome_linked_list.py) | Easy | ✅ |

---

## 🔃 经典排序算法 · `sorting/`

| 算法 | 文件 | 平均复杂度 | 稳定性 |
|---|---|---|---|
| 冒泡排序 | [bubble_sort.py](sorting/bubble_sort.py) | $O(n^2)$ | 稳定 |
| 选择排序 | [selection_sort.py](sorting/selection_sort.py) | $O(n^2)$ | 不稳定 |
| 插入排序 | [insertion_sort.py](sorting/insertion_sort.py) | $O(n^2)$ | 稳定 |
| 归并排序(朴素) | [merge_sort_naive.py](sorting/merge_sort_naive.py) | $O(n\log n)$ | 稳定 |
| 归并排序 | [merge_sort.py](sorting/merge_sort.py) | $O(n\log n)$ | 稳定 |
| 三路快排 | [three_way_quick_sort.py](sorting/three_way_quick_sort.py) | $O(n\log n)$ | 不稳定 |
| 堆排序 | [heap_sort.py](sorting/heap_sort.py) | $O(n\log n)$ | 不稳定 |
| 计数排序 | [counting_sort.py](sorting/counting_sort.py) | $O(n+k)$ | 稳定 |
| 桶排序 | [bucket_sort.py](sorting/bucket_sort.py) | $O(n+k)$ | 稳定 |
| 基数排序 | [radix_sort.py](sorting/radix_sort.py) | $O(nk)$ | 稳定 |

### 延伸应用 · `sorting/problems/`

| 问题 | 文件 | 核心思想 |
|---|---|---|
| 荷兰国旗问题 | [problem_dutch_national_flag.py](sorting/problems/problem_dutch_national_flag.py) | 三路划分 partition |
| 小和问题 | [problem_small_sum.py](sorting/problems/problem_small_sum.py) | 归并排序 |
| 数组中的逆序对 | [problem_invertion_count.py](sorting/problems/problem_invertion_count.py) | 归并排序 |

---

## 📝 笔记 · `notes/`

存放**跨题型**的通用专题总结,例如 Python 语法、面试技巧、复杂度推导等。

- [python_oop_basics.md](notes/python_oop_basics.md) — 类 / 对象 / `self` / `__init__` / 魔术方法 / 参数 / 变量 vs 对象（链表理解的前置知识）

> 另有 **章节笔记**: 每个题型文件夹内都有一份 `notes.md`(如 `leetcode/stack/notes.md`),
> 记录该章节的**识别信号、可复用模板、踩坑回顾、复杂度速查、面试口述稿**。

---

## ▶️ 运行方式

需要 Python 3.10+,无第三方依赖:

```bash
python leetcode/array_hashing/1_two_sum.py
python sorting/merge_sort.py
```

### 🧪 链表题的本地自测脚手架

力扣的链表题把**头当参数**传进来（`Solution` 里**没有** `self.head`），网页上写的
`head = [1,2,3,4,5]` 只是**展示格式**,实际收到的是 `ListNode`（`val` / `next`）。

因此 `leetcode/linked_list/` 下每个骨架文件底部都带同一套脚手架
(**完整解法文件里为激活态;骨架文件里为注释态,取消注释即可自测**):

```python
class ListNode(object):          # 力扣环境自带,本地需要自己补
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def build(arr):                  # [1,2,3] -> 1->2->3（复刻判题机的构造过程）
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_array(head):              # 链表 -> [1,2,3]（方便和期望结果对照）
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
```

用法一行搞定:

```python
print(to_array(sol.reverseList(build([1, 2, 3, 4, 5]))))   # 期望 [5, 4, 3, 2, 1]
```

> ⚠️ **提交力扣前务必把整段脚手架注释掉**（力扣自带 `ListNode`,重复定义会报错）。
> 原理与踩坑详见 [leetcode/linked_list/notes.md](leetcode/linked_list/notes.md) 的 §5.2 / §5.3。

---

## 🔐 Git 推送(SSH over 443)

本机直连 `github.com:443` 常被网络阻断,而 `ssh.github.com:443` 可用,因此采用 SSH 并强制走 443 端口:

- `~/.ssh/config` 中已把 `github.com` 映射到 `ssh.github.com` 的 **443** 端口;
- 本仓库远程使用 SSH:`git@github.com:Tanking020/algorithm-journey.git`。

**新克隆仓库时**:请选择 **SSH** 地址(`git@github.com:...`);若已用 HTTPS 克隆,执行一条命令切换:

```bash
git remote set-url origin git@github.com:<用户名>/<仓库名>.git
```

**自检**:

```bash
ssh -T git@github.com     # 看到 "Hi Tanking020! You've successfully authenticated" 即为正常
```

---

## 📌 说明

- 每个解法文件内部保留了从暴力到最优的演进过程,早期版本以注释形式存在。
- 部分题目内含多种解法对比(如 155 Min Stack 保留"双栈"与"单栈+元组"两种),便于权衡取舍。
- 题目按**题型**归类,文件名保留题号前缀,便于按号检索。
- 链表题统一带 `build` / `to_array` 本地自测脚手架(见上文「🧪 链表题的本地自测脚手架」)。
