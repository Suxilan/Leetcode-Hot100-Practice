"""LeetCode 148 - Sort List (ACM style)."""

import sys
import io

LEETCODE_ID = 148
TITLE = "Sort List"
CATEGORY = "linked_list"
DIFFICULTY = "Medium"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Input format:
# Space-separated integers representing the linked list
# Output format:
# Space-separated integers representing the sorted linked list
SAMPLE_CASES = [
    ("4 2 1 3\n", "1 2 3 4\n"),
    ("-1 5 3 4 0\n", "-1 0 3 4 5\n"),
    ("\n", "\n"),
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
    
    dummy = ListNode()
    curr = dummy
    for val in data:
        curr.next = ListNode(int(val))
        curr = curr.next
    head = dummy.next
    
    # 你的代码写在这里...
    # 需要返回修改后的 head，并利用归并排序保证 O(n log n) 时间复杂度和 O(1) 空间
    
    # 打印结果
    ans = []
    # 假设你修改完的头节点叫 sorted_head
    sorted_head = head # 替换为你的返回结果
    while sorted_head:
        ans.append(str(sorted_head.val))
        sorted_head = sorted_head.next
    print(" ".join(ans))

if __name__ == "__main__":
    check(solve)
