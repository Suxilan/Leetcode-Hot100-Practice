"""LeetCode 124 - Binary Tree Maximum Path Sum (ACM style)."""

import sys
import io

LEETCODE_ID = 124
TITLE = "Binary Tree Maximum Path Sum"
CATEGORY = "binary_tree"
DIFFICULTY = "Hard"

# Input format:
# Line 1: space-separated tree node values in level-order. "null" represents an empty node.
# Output format:
# One integer representing the maximum path sum.
SAMPLE_CASES = [
    (
        "1 2 3\n",
        "6\n"
    ),
    (
        "-10 9 20 null null 15 7\n",
        "42\n"
    ),
    (
        "-3\n",
        "-3\n"
    ),
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

# =========================================================================
# Your implementation area (Strict ACM Mode):
# Use sys.stdin.read() or import sys to get inputs, and print() to output.
# You can submit the exact solve() function to the actual test platform!
# =========================================================================

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
        
    # TODO: Define TreeNode, build the tree, compute maximum path sum and print()
    pass

if __name__ == "__main__":
    check(solve)