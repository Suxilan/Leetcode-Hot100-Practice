"""LeetCode 236 - Lowest Common Ancestor of a Binary Tree (ACM style)."""

import sys
import io

LEETCODE_ID = 236
TITLE = "Lowest Common Ancestor of a Binary Tree"
CATEGORY = "binary_tree"
DIFFICULTY = "Medium"

# Input format:
# Line 1: space-separated tree node values in level-order. "null" represents an empty node.
# Line 2: value of node p
# Line 3: value of node q
# Output format:
# One integer, the value of the Lowest Common Ancestor node.
SAMPLE_CASES = [
    (
        "3 5 1 6 2 0 8 null null 7 4\n5\n1\n",
        "3\n"
    ),
    (
        "3 5 1 6 2 0 8 null null 7 4\n5\n4\n",
        "5\n"
    ),
    (
        "1 2\n1\n2\n",
        "1\n"
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
        
    # 'data' has tree nodes, then p's value, then q's value
    # You can extract p and q by taking data[-2] and data[-1], 
    # and the tree sequence is data[:-2].
    
    # TODO: Define TreeNode, build the tree, find the LCA, and print() its value
    pass

if __name__ == "__main__":
    check(solve)
