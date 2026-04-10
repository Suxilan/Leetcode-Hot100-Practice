"""LeetCode 560 - Subarray Sum Equals K (ACM style)."""

import sys
import io

LEETCODE_ID = 560
TITLE = "Subarray Sum Equals K"
CATEGORY = "prefix_sum"
DIFFICULTY = "Medium"

# Input format:
# Line 1: n k
# Line 2: n integers
# Output format:
# One integer, count of subarrays with sum = k.
SAMPLE_CASES = [
    ("3 2\n1 1 1\n", "2\n"),
    ("3 3\n1 2 3\n", "2\n"),
    ("5 0\n1 -1 0 2 -2\n", "6\n"),
]


def check(solve_func) -> bool:
    def _normalize(text: str) -> str:
        lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
        return "\n".join(lines)

    all_passed = True
    for i, (inp, expected) in enumerate(SAMPLE_CASES, start=1):
        sys.stdin = io.StringIO(inp)
        captured_out = io.StringIO()
        sys.stdout = captured_out

        try:
            solve_func()
        except Exception as e:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
            print(f"[FAIL] case#{i} - Exception: {e}")
            all_passed = False
            continue
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

        actual = captured_out.getvalue()
        if _normalize(actual) != _normalize(expected):
            all_passed = False
            print(f"[FAIL] case#{i}")
            print("  input   :", repr(inp))
            print("  expected:", repr(expected))
            print("  actual  :", repr(actual))
        else:
            print(f"[PASS] case#{i}")
    return all_passed


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    # TODO: Implement prefix-sum + hashmap in O(n).
    pass


if __name__ == "__main__":
    check(solve)
