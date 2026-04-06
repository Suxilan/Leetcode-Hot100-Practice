"""LeetCode 300 - Longest Increasing Subsequence (ACM style)."""

import sys
import io

LEETCODE_ID = 300
TITLE = "Longest Increasing Subsequence"
CATEGORY = "dynamic_programming"
DIFFICULTY = "Medium"

# Input format:
# Line 1: n
# Line 2: n integers
# Output format:
# One integer, the LIS length.
SAMPLE_CASES = [
    ("8\n10 9 2 5 3 7 101 18\n", "4\n"),
    ("6\n0 1 0 3 2 3\n", "4\n"),
    ("4\n7 7 7 7\n", "1\n"),
]


def check(solve_func) -> bool:
    """Run built-in test cases automatically by mocking sys.stdin and sys.stdout."""

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


# =========================================================================
# Your implementation area (Strict ACM Mode):
# Use sys.stdin.read() or import sys to get inputs, and print() to output.
# You can submit the exact solve() function to the actual test platform!
# =========================================================================

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    # TODO: Implement LIS.
    # Option A: O(n^2) DP for interviews.
    # Option B: O(n log n) patience sorting for performance.
    pass


if __name__ == "__main__":
    check(solve)
