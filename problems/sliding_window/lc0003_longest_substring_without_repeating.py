"""LeetCode 3 - Longest Substring Without Repeating Characters (ACM style)."""

import sys

LEETCODE_ID = 3
TITLE = "Longest Substring Without Repeating Characters"
CATEGORY = "sliding_window"
DIFFICULTY = "Medium"

SAMPLE_CASES = [
    ("abcabcbb\n", "3\n"),
    ("bbbbb\n", "1\n"),
    ("pwwkew\n", "3\n"),
    ("\n", "0\n"),
]


def length_of_longest_substring_core(s: str) -> int:
    """LeetCode core logic placeholder: return max length without repeat."""
    # TODO: Replace with your own LeetCode core implementation.
    left = 0
    last = {}
    ans = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        ans = max(ans, right - left + 1)
    return ans


def solve() -> None:
    s = sys.stdin.readline().rstrip("\n")
    ans = length_of_longest_substring_core(s)
    print(ans)


if __name__ == "__main__":
    solve()
