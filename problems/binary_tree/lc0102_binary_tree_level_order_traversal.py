"""LeetCode 102 - Binary Tree Level Order Traversal (ACM style)."""

import sys
import io

LEETCODE_ID = 102
TITLE = "Binary Tree Level Order Traversal"
CATEGORY = "binary_tree"
DIFFICULTY = "Medium"

# Input format:
# Line 1: space-separated tree node values in level-order. "null" represents an empty node.
# Output format:
# Multiple lines, each line containing space-separated values for one level of the tree.
SAMPLE_CASES = [
    (
        "3 9 20 null null 15 7\n",
        "3\n9 20\n15 7\n"
    ),
    (
        "1\n",
        "1\n"
    ),
    (
        "\n",
        "\n"
    ),
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
    # Read all tokens at once
    data = sys.stdin.read().split()
    if not data:
        return
        
    # TODO: Define TreeNode, build the tree from level-order 'data' array, 
    # run your level-order traversal, and print() each level on a new line.
    pass

if __name__ == "__main__":
    # Local check (Mocking input/output):
    check(solve)

    # For real submission in platforms like Nowcoder, keep ONLY this:
    # solve()
