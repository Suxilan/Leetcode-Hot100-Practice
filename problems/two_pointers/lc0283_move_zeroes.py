"""LeetCode 283 - Move Zeroes (ACM style)."""

import sys
import io

LEETCODE_ID = 283
TITLE = "Move Zeroes"
CATEGORY = "two_pointers"
DIFFICULTY = "Easy"

SAMPLE_CASES = [
    ("5\n0 1 0 3 12\n", "1 3 12 0 0\n"),
    ("4\n0 0 0 0\n", "0 0 0 0\n"),
    ("4\n1 2 3 4\n", "1 2 3 4\n"),
]

def check(solve_func) -> bool:
    """Run built-in test cases automatically by mocking sys.stdin and sys.stdout."""
    def _normalize(text: str) -> str:
        lines = [line.rstrip() for line in text.splitlines()]
        while lines and lines[-1] == "":
            lines.pop()
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
    # Read all tokens at once (handles any whitespace/newlines automatically)
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    if n == 0:
        print()
        return
        
    # Simply slice the data array
    nums = [int(x) for x in data[1:n+1]]
    
    print(nums)

    # Move Zeroes logic


if __name__ == "__main__":
    # Local check (Mocking input/output):
    check(solve)

    # For real submission in platforms like Nowcoder, keep ONLY this:
    # solve()

