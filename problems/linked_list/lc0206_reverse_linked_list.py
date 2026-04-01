"""LeetCode 206 - Reverse Linked List (ACM style)."""

import sys
import io

LEETCODE_ID = 206
TITLE = "Reverse Linked List"
CATEGORY = "linked_list"
DIFFICULTY = "Easy"

SAMPLE_CASES = [
    ("5\n1 2 3 4 5\n", "5 4 3 2 1\n"),
    ("1\n7\n", "7\n"),
    ("0\n\n", "\n"),
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
        # Setup mock stdin/stdout
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
            # Restore 
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

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve():
    # Read all tokens at once (handles any whitespace/newlines automatically)
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    if n == 0:
        print()
        return
        
    vals = [int(x) for x in data[1:n+1]]

    # Deserialize to Linked List
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    head = dummy.next

    # Core logic: Reverse linked list
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    new_head = prev

    # Serialize and Print
    result = []
    curr = new_head
    while curr:
        result.append(str(curr.val))
        curr = curr.next

    print(" ".join(result))

if __name__ == "__main__":
    # Local check (Mocking input/output):
    check(solve)

    # For real submission in platforms like Nowcoder, keep ONLY this:
    # solve()
