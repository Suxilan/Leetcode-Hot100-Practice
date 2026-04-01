"""LeetCode 3 - Longest Substring Without Repeating Characters (ACM style)."""

import sys
import io

LEETCODE_ID = 3
TITLE = "Longest Substring Without Repeating Characters"
CATEGORY = "sliding_window"
DIFFICULTY = "Medium"

SAMPLE_CASES = [
    ("abcabcbb\n", "3\n"),
    ("bbbbb\n", "1\n"),
    ("pwwkew\n", "3\n"),
    ("\n", "0\n"),
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
    # Use readline() directly if problem inputs are line-separated text
    # e.g., a single string in the first line
    line = sys.stdin.readline()
    if not line:
        return
        
    s = line.rstrip('\n')
    
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    print(max_length)

if __name__ == "__main__":
    # Local check (Mocking input/output):
    check(solve)

    # For real submission in platforms like Nowcoder, keep ONLY this:
    # solve()
