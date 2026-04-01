# 题目索引（按题型分类）

## 链表

- LC206 Reverse Linked List
- 脚本: [problems/linked_list/lc0206_reverse_linked_list.py](../problems/linked_list/lc0206_reverse_linked_list.py)

## 双指针

- LC283 Move Zeroes
- 脚本: [problems/two_pointers/lc0283_move_zeroes.py](../problems/two_pointers/lc0283_move_zeroes.py)

## 滑动窗口

- LC3 Longest Substring Without Repeating Characters
- 脚本: [problems/sliding_window/lc0003_longest_substring_without_repeating.py](../problems/sliding_window/lc0003_longest_substring_without_repeating.py)

## 使用说明

- 脚本内部自带 `SAMPLE_CASES` 并附带自动化 `check()` 测试机制。
- 开发者必须在此基础上实现全流程 ACM 逻辑，包含数据结构（如 `ListNode`）定义、核心算法逻辑、文本数据的安全反序列化和序列化。
- 把你的逻辑写在 `solve()` 方法内部。在这个区域你直接调用 `sys.stdin.read()` 并往 `print()` 中输出内容。这与华为、美团的笔试体验完全一致。
- 开发时，使用 `check(solve)` 执行全部用例。提交时只需复制 `solve()` 主体代码到赛题界面即可。
