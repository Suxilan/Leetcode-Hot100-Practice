"""LeetCode 31 - Next Permutation (ACM style)."""

import sys
import io

LEETCODE_ID = 31
TITLE = "Next Permutation"
CATEGORY = "array"
DIFFICULTY = "Medium"

# Input format:
# n integers representing the array
# Output format:
# Space-separated integers representing the next permutation.
SAMPLE_CASES = [
    ("1 2 3\n", "1 3 2\n"),
    ("3 2 1\n", "1 2 3\n"),
    ("1 1 5\n", "1 5 1\n"),
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
    
    nums = list(map(int, data))
    
    # 你的代码写在这里...
    # 注意题目要求原地修改 nums
    
    print(" ".join(map(str, nums)))

if __name__ == "__main__":
    check(solve)
