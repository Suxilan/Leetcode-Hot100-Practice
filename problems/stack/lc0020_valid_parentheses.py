"""LeetCode 20 - Valid Parentheses (ACM style)."""

import sys
import io

LEETCODE_ID = 20
TITLE = "Valid Parentheses"
CATEGORY = "stack"
DIFFICULTY = "Easy"

# Input format:
# Line 1: one parentheses string s
# Output format:
# true / false (lowercase)
SAMPLE_CASES = [
    ("()\n", "true\n"),
    ("()[]{}\n", "true\n"),
    ("(]\n", "false\n"),
    ("([)]\n", "false\n"),
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
    line = sys.stdin.readline()
    if not line:
        return

    # TODO: Implement stack-based parentheses validation.
    pass


if __name__ == "__main__":
    check(solve)
