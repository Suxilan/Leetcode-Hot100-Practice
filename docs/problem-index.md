# 题目索引（按题型分类）

## 链表

- LC206 Reverse Linked List
- 脚本: [problems/linked_list/lc0206_reverse_linked_list.py](../problems/linked_list/lc0206_reverse_linked_list.py)

## 双指针

- LC283 Move Zeroes
- 脚本: [problems/two_pointers/lc0283_move_zeroes.py](../problems/two_pointers/lc0283_move_zeroes.py)

- LC42 Trapping Rain Water
- 脚本: [problems/two_pointers/lc0042_trapping_rain_water.py](../problems/two_pointers/lc0042_trapping_rain_water.py)

## 滑动窗口

- LC3 Longest Substring Without Repeating Characters
- 脚本: [problems/sliding_window/lc0003_longest_substring_without_repeating.py](../problems/sliding_window/lc0003_longest_substring_without_repeating.py)

- LC239 Sliding Window Maximum
- 脚本: [problems/sliding_window/lc0239_sliding_window_maximum.py](../problems/sliding_window/lc0239_sliding_window_maximum.py)

## 单调栈

- LC739 Daily Temperatures
- 脚本: [problems/monotonic_stack/lc0739_daily_temperatures.py](../problems/monotonic_stack/lc0739_daily_temperatures.py)

- LC84 Largest Rectangle in Histogram
- 脚本: [problems/monotonic_stack/lc0084_largest_rectangle_in_histogram.py](../problems/monotonic_stack/lc0084_largest_rectangle_in_histogram.py)

## 二分查找

- LC33 Search in Rotated Sorted Array
- 脚本: [problems/binary_search/lc0033_search_in_rotated_sorted_array.py](../problems/binary_search/lc0033_search_in_rotated_sorted_array.py)

## 二叉树

- LC102 Binary Tree Level Order Traversal
- 脚本: [problems/binary_tree/lc0102_binary_tree_level_order_traversal.py](../problems/binary_tree/lc0102_binary_tree_level_order_traversal.py)

- LC236 Lowest Common Ancestor of a Binary Tree
- 脚本: [problems/binary_tree/lc0236_lowest_common_ancestor.py](../problems/binary_tree/lc0236_lowest_common_ancestor.py)

- LC124 Binary Tree Maximum Path Sum
- 脚本: [problems/binary_tree/lc0124_binary_tree_maximum_path_sum.py](../problems/binary_tree/lc0124_binary_tree_maximum_path_sum.py)

## 动态规划

- LC70 Climbing Stairs
- 脚本: [problems/dynamic_programming/lc0070_climbing_stairs.py](../problems/dynamic_programming/lc0070_climbing_stairs.py)

- LC322 Coin Change
- 脚本: [problems/dynamic_programming/lc0322_coin_change.py](../problems/dynamic_programming/lc0322_coin_change.py)

- LC300 Longest Increasing Subsequence
- 脚本: [problems/dynamic_programming/lc0300_longest_increasing_subsequence.py](../problems/dynamic_programming/lc0300_longest_increasing_subsequence.py)

## 回溯

- LC46 Permutations
- 脚本: [problems/backtracking/lc0046_permutations.py](../problems/backtracking/lc0046_permutations.py)

- LC78 Subsets
- 脚本: [problems/backtracking/lc0078_subsets.py](../problems/backtracking/lc0078_subsets.py)

## 矩阵

- LC200 Number of Islands
- 脚本: [problems/matrix/lc0200_number_of_islands.py](../problems/matrix/lc0200_number_of_islands.py)

## 数组模拟

- LC54 Spiral Matrix
- 脚本: [problems/array/lc0054_spiral_matrix.py](../problems/array/lc0054_spiral_matrix.py)

## 设计

- LC146 LRU Cache
- 脚本: [problems/design/lc0146_lru_cache.py](../problems/design/lc0146_lru_cache.py)

## 使用说明

- 脚本内部自带 `SAMPLE_CASES` 并附带自动化 `check()` 测试机制。
- 开发者必须在此基础上实现全流程 ACM 逻辑，包含数据结构（如 `ListNode`）定义、核心算法逻辑、文本数据的安全反序列化和序列化。
- 把你的逻辑写在 `solve()` 方法内部。在这个区域你直接调用 `sys.stdin.read()` 并往 `print()` 中输出内容。这与华为、美团的笔试体验完全一致。
- 开发时，使用 `check(solve)` 执行全部用例。提交时只需复制 `solve()` 主体代码到赛题界面即可。
