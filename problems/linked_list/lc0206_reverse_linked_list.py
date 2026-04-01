"""LeetCode 206 - Reverse Linked List (ACM style)."""

import sys

LEETCODE_ID = 206
TITLE = "Reverse Linked List"
CATEGORY = "linked_list"
DIFFICULTY = "Easy"

SAMPLE_CASES = [
    ("5\n1 2 3 4 5\n", "5 4 3 2 1\n"),
    ("1\n7\n", "7\n"),
    ("0\n\n", "\n"),
]


def reverse_list_core(nums):
    """LeetCode core logic placeholder: input list, output reversed list."""
    # TODO: Replace with your own LeetCode core implementation.
    return nums[::-1]


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    nums = list(map(int, data[1:1 + n]))
    ans = reverse_list_core(nums)

    if ans:
        print(*ans)
    else:
        print()


if __name__ == "__main__":
    solve()
