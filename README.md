# Leetcode Hot100 Practice (ACM Mode)

该仓库用于面向笔试场景的 ACM 模式刷题。

## 目录结构（按题型分类）

- `problems/linked_list/`：链表题
- `problems/two_pointers/`：双指针题
- `problems/sliding_window/`：滑动窗口题
- `problems/binary_tree/`：二叉树题
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

说明：
- 每个脚本包含题号、题型、题意、输入输出描述、测试样例与边界数据。
- 每个脚本都预留了 `def solve():` 方法，使用 `sys.stdin` 读取数据、`print()` 输出。你将体会到和真实 牛客/Codeforces 笔试环境100%一致的开发手感。
- 脚本内置的 `check()` 方法通过 `io.StringIO` 动态劫持标准输入输出，以黑盒方式执行 `solve()`，自动跑完全部测试用例并反馈。
- 你可以**完全手敲代码**：包括数据结构定义、读入反序列化、核心算法、文本输出。保持 LeetCode 核心逻辑手感的同时，锻炼笔试所需的一次性 AC（通过）能力。
