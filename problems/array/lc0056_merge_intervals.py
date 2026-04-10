"""LeetCode 56 - Merge Intervals (ACM style)."""

import sys
import io

LEETCODE_ID = 56
TITLE = "Merge Intervals"
CATEGORY = "array"
DIFFICULTY = "Medium"

# Input format:
# Line 1: n
# Next n lines: l r
# Output format:
# Multiple lines, each line one merged interval: l r
SAMPLE_CASES = [
    ("4\n1 3\n2 6\n8 10\n15 18\n", "1 6\n8 10\n15 18\n"),
    ("2\n1 4\n4 5\n", "1 5\n"),
    ("1\n1 2\n", "1 2\n"),
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

    # TODO: Implement sort + greedy merge.
    pass


if __name__ == "__main__":
    check(solve)
