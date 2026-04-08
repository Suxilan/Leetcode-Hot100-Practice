"""LeetCode 239 - Sliding Window Maximum (ACM style)."""

import sys
import io

LEETCODE_ID = 239
TITLE = "Sliding Window Maximum"
CATEGORY = "sliding_window"
DIFFICULTY = "Hard"

# Input format:
# Line 1: n k
# Line 2: n integers, nums
# Output format:
# One line with max value for each window.
SAMPLE_CASES = [
    ("8 3\n1 3 -1 -3 5 3 6 7\n", "3 3 5 5 6 7\n"),
    ("1 1\n1\n", "1\n"),
    ("5 2\n9 10 9 -7 -4\n", "10 10 9 -4\n"),
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

    # TODO: Implement monotonic deque solution.
    pass


if __name__ == "__main__":
    check(solve)
