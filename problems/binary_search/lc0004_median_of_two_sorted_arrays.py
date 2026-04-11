"""LeetCode 4 - Median of Two Sorted Arrays (ACM style)."""

import sys
import io

LEETCODE_ID = 4
TITLE = "Median of Two Sorted Arrays"
CATEGORY = "binary_search"
DIFFICULTY = "Hard"

# Input format:
# Line 1: m n (lengths of arrays)
# Line 2: m integers (nums1)
# Line 3: n integers (nums2)
# Output format:
# A single float number representing the median.
SAMPLE_CASES = [
    ("2 2\n1 3\n2\n", "2.0\n"),
    ("2 2\n1 2\n3 4\n", "2.5\n"),
    ("0 1\n\n1\n", "1.0\n"),
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
    
    m, n = int(data[0]), int(data[1])
    nums1 = list(map(int, data[2:2+m]))
    nums2 = list(map(int, data[2+m:2+m+n]))
    
    # 你的代码写在这里...
    pass

if __name__ == "__main__":
    check(solve)
