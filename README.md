# Algorithm Journey

> LeetCode solutions & classic sorting algorithms, with brute-force → optimal evolution and detailed annotations.

个人算法学习记录。每道题的解法文件都保留了从**暴力解 → 逐步优化 → 最优解**的完整演进过程,
早期方案以注释形式留在同一个文件中,方便日后回顾思路变化,而不只是看一个"标准答案"。

---

## 📁 目录结构

```
algorithm-journey/
├── leetcode/               # LeetCode 题解(按题型分类)
│   ├── array_hashing/      # 数组 & 哈希表
│   ├── two_pointers/       # 双指针
│   ├── sliding_window/     # 滑动窗口
│   └── stack/              # 栈
├── sorting/                # 经典排序算法
│   └── problems/           # 排序思想的延伸应用(逆序对、小和、荷兰国旗)
├── notes/                  # 专题笔记与跨题总结
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
| 84 | [Largest Rectangle in Histogram](leetcode/stack/84_largest_rectangle_in_histogram.py) | Hard | ⬜ |
| 155 | [Min Stack](leetcode/stack/155_min_stack.py) | Medium | ⬜ |
| 739 | [Daily Temperatures](leetcode/stack/739_daily_temperatures.py) | Medium | ⬜ |

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

存放跨题专题总结,例如算法模板、边界条件讨论、复杂度推导等。

---

## ▶️ 运行方式

需要 Python 3.10+,无第三方依赖:

```bash
python leetcode/array_hashing/1_two_sum.py
python sorting/merge_sort.py
```

---

## � Git 推送(SSH over 443)

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

## �📌 说明

- 每个解法文件内部保留了从暴力到最优的演进过程,早期版本以注释形式存在。
- 题目按**题型**归类,文件名保留题号前缀,便于按号检索。
