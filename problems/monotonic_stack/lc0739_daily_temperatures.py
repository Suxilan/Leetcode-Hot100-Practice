"""LeetCode 739 - Daily Temperatures (ACM style)."""

import sys
import io

LEETCODE_ID = 739
TITLE = "Daily Temperatures"
CATEGORY = "monotonic_stack"
DIFFICULTY = "Medium"

# Input format:
# Line 1: n
# Line 2: n integers, temperatures
# Output format:
# One line with n integers, waiting days.
SAMPLE_CASES = [
    ("8\n73 74 75 71 69 72 76 73\n", "1 1 4 2 1 1 0 0\n"),
    ("4\n30 40 50 60\n", "1 1 1 0\n"),
    ("3\n30 60 90\n", "1 1 0\n"),
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

    # TODO: Implement monotonic stack (store indices).
    pass


if __name__ == "__main__":
    check(solve)
