"""LeetCode 206 - Reverse Linked List (ACM style)."""

import sys

LEETCODE_ID = 206
TITLE = "Reverse Linked List"
CATEGORY = "linked_list"
DIFFICULTY = "Easy"

SAMPLE_CASES = [
    ("5\n1 2 3 4 5\n", "5 4 3 2 1\n"),
    ("1\n7\n", "7\n"),
    ("0\n\n", "\n"),
]

def check(solver) -> bool:
    """Run built-in test cases against solver(input_str) -> output_str."""
    def _normalize(text: str) -> str:
        lines = [line.rstrip() for line in text.splitlines()]
        while lines and lines[-1] == "":
            lines.pop()
        return "\n".join(lines)

    all_passed = True
    for i, (inp, expected) in enumerate(SAMPLE_CASES, start=1):
        actual = solver(inp)
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
# 以下为你的作答区。你必须完整实现节点定义、反序列化(建表)、算法核心逻辑、以及序列化(输出结果)。
# =========================================================================

# TODO: 像你在 ACM / 笔试中一样，定义数据结构，实现完整的解析、执行和输出组装。
def solver_stub(input_str: str) -> str:
    """Read full input string, run the full solution, return formatted string."""
    return ""

if __name__ == "__main__":
    # 你可以在本地开发时用 check() 验证你的 solver_stub:
    check(solver_stub)

