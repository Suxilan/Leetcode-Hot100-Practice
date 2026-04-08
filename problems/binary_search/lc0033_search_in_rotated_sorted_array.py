"""LeetCode 33 - Search in Rotated Sorted Array (ACM style)."""

import sys
import io

LEETCODE_ID = 33
TITLE = "Search in Rotated Sorted Array"
CATEGORY = "binary_search"
DIFFICULTY = "Medium"

# Input format:
# Line 1: n target
# Line 2: n integers, nums
# Output format:
# One integer index, or -1 if not found.
SAMPLE_CASES = [
    ("7 0\n4 5 6 7 0 1 2\n", "4\n"),
    ("7 3\n4 5 6 7 0 1 2\n", "-1\n"),
    ("1 0\n1\n", "-1\n"),
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

    # TODO: Implement rotated-array binary search with careful <= boundary checks.
    pass


if __name__ == "__main__":
    check(solve)
