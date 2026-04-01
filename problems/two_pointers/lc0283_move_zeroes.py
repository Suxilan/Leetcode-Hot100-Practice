"""LeetCode 283 - Move Zeroes (ACM style)."""

import sys

LEETCODE_ID = 283
TITLE = "Move Zeroes"
CATEGORY = "two_pointers"
DIFFICULTY = "Easy"

SAMPLE_CASES = [
    ("5\n0 1 0 3 12\n", "1 3 12 0 0\n"),
    ("4\n0 0 0 0\n", "0 0 0 0\n"),
    ("4\n1 2 3 4\n", "1 2 3 4\n"),
]


def move_zeroes_core(nums):
    """LeetCode core logic placeholder: in-place move zeroes, return nums."""
    # TODO: Replace with your own LeetCode core implementation.
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    nums = list(map(int, data[1:1 + n]))
    ans = move_zeroes_core(nums)

    if n > 0:
        print(*ans)
    else:
        print()


if __name__ == "__main__":
    solve()
