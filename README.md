# Leetcode Hot100 Practice (ACM Mode)

该仓库用于面向笔试场景的 ACM 模式刷题。

## 目录结构（按题型分类）

- `problems/linked_list/`：链表题
- `problems/two_pointers/`：双指针题
- `problems/sliding_window/`：滑动窗口题
- `problems/binary_tree/`：二叉树题
- `problems/dynamic_programming/`：动态规划题
- `problems/backtracking/`：回溯题
- `problems/matrix/`：矩阵题
- `problems/array/`：数组模拟题
- `problems/monotonic_stack/`：单调栈题
- `problems/binary_search/`：二分查找题
- `problems/prefix_sum/`：前缀和题
- `problems/heap/`：堆与选择题
- `problems/stack/`：栈基础题
- `problems/design/`：数据结构设计题
- `docs/`：题型整理与解法归纳

## Docs

- 题目索引（含脚本超链接）：[docs/problem-index.md](docs/problem-index.md)
- 解法归纳总结：[docs/solution-summary.md](docs/solution-summary.md)

## 当前已整理题目（每题一个脚本，仅含题目数据与样例）

1. [problems/linked_list/lc0206_reverse_linked_list.py](problems/linked_list/lc0206_reverse_linked_list.py)
2. [problems/two_pointers/lc0283_move_zeroes.py](problems/two_pointers/lc0283_move_zeroes.py)
3. [problems/sliding_window/lc0003_longest_substring_without_repeating.py](problems/sliding_window/lc0003_longest_substring_without_repeating.py)
4. [problems/binary_tree/lc0102_binary_tree_level_order_traversal.py](problems/binary_tree/lc0102_binary_tree_level_order_traversal.py)
5. [problems/binary_tree/lc0236_lowest_common_ancestor.py](problems/binary_tree/lc0236_lowest_common_ancestor.py)
6. [problems/binary_tree/lc0124_binary_tree_maximum_path_sum.py](problems/binary_tree/lc0124_binary_tree_maximum_path_sum.py)
7. [problems/dynamic_programming/lc0070_climbing_stairs.py](problems/dynamic_programming/lc0070_climbing_stairs.py)
8. [problems/dynamic_programming/lc0322_coin_change.py](problems/dynamic_programming/lc0322_coin_change.py)
9. [problems/dynamic_programming/lc0300_longest_increasing_subsequence.py](problems/dynamic_programming/lc0300_longest_increasing_subsequence.py)
10. [problems/backtracking/lc0046_permutations.py](problems/backtracking/lc0046_permutations.py)
11. [problems/backtracking/lc0078_subsets.py](problems/backtracking/lc0078_subsets.py)
12. [problems/matrix/lc0200_number_of_islands.py](problems/matrix/lc0200_number_of_islands.py)
13. [problems/array/lc0054_spiral_matrix.py](problems/array/lc0054_spiral_matrix.py)
14. [problems/design/lc0146_lru_cache.py](problems/design/lc0146_lru_cache.py)
15. [problems/two_pointers/lc0042_trapping_rain_water.py](problems/two_pointers/lc0042_trapping_rain_water.py)
16. [problems/monotonic_stack/lc0739_daily_temperatures.py](problems/monotonic_stack/lc0739_daily_temperatures.py)
17. [problems/monotonic_stack/lc0084_largest_rectangle_in_histogram.py](problems/monotonic_stack/lc0084_largest_rectangle_in_histogram.py)
18. [problems/sliding_window/lc0239_sliding_window_maximum.py](problems/sliding_window/lc0239_sliding_window_maximum.py)
19. [problems/binary_search/lc0033_search_in_rotated_sorted_array.py](problems/binary_search/lc0033_search_in_rotated_sorted_array.py)
20. [problems/two_pointers/lc0015_3sum.py](problems/two_pointers/lc0015_3sum.py)
21. [problems/array/lc0056_merge_intervals.py](problems/array/lc0056_merge_intervals.py)
22. [problems/prefix_sum/lc0560_subarray_sum_equals_k.py](problems/prefix_sum/lc0560_subarray_sum_equals_k.py)
23. [problems/heap/lc0215_kth_largest_element_in_an_array.py](problems/heap/lc0215_kth_largest_element_in_an_array.py)
24. [problems/stack/lc0020_valid_parentheses.py](problems/stack/lc0020_valid_parentheses.py)
25. [problems/binary_search/lc0004_median_of_two_sorted_arrays.py](problems/binary_search/lc0004_median_of_two_sorted_arrays.py)
26. [problems/array/lc0031_next_permutation.py](problems/array/lc0031_next_permutation.py)
27. [problems/linked_list/lc0148_sort_list.py](problems/linked_list/lc0148_sort_list.py)

说明：
- 每个脚本包含题号、题型、题意、输入输出描述、测试样例与边界数据。
- 每个脚本都预留了 `def solve():` 方法，使用 `sys.stdin` 读取数据、`print()` 输出。你将体会到和真实 牛客/Codeforces 笔试环境100%一致的开发手感。
- 脚本内置的 `check()` 方法通过 `io.StringIO` 动态劫持标准输入输出，以黑盒方式执行 `solve()`，自动跑完全部测试用例并反馈。
- 你可以**完全手敲代码**：包括数据结构定义、读入反序列化、核心算法、文本输出。保持 LeetCode 核心逻辑手感的同时，锻炼笔试所需的一次性 AC（通过）能力。
