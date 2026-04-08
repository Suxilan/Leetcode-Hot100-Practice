"""LeetCode 84 - Largest Rectangle in Histogram (ACM style)."""

import sys
import io

LEETCODE_ID = 84
TITLE = "Largest Rectangle in Histogram"
CATEGORY = "monotonic_stack"
DIFFICULTY = "Hard"

# Input format:
# Line 1: n
# Line 2: n integers, heights
# Output format:
# One integer, max rectangle area.
SAMPLE_CASES = [
    ("6\n2 1 5 6 2 3\n", "10\n"),
    ("2\n2 4\n", "4\n"),
    ("5\n1 1 1 1 1\n", "5\n"),
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

    # TODO: Implement monotonic increasing stack (store indices, sentinel trick).
    pass


if __name__ == "__main__":
    check(solve)
