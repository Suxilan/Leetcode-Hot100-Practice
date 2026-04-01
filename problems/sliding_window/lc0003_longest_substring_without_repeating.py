"""LeetCode 3 - Longest Substring Without Repeating Characters (ACM style)."""

import sys

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
# 以下为你的作答区。你必须完整实现输入解析、算法核心逻辑、以及输出组装。
# =========================================================================

# TODO: 像你在 ACM / 笔试中一样，完整的进行输入获取、反序列化、业务逻辑和文本打印逻辑。
# 你可以直接在此编写你的解答函数。
def solver_stub(input_str: str) -> str:
    """Read full input string, run the full solution, return formatted string."""
    return ""

if __name__ == "__main__":
    # 你可以在本地开发时用 check() 验证你的 solver_stub:
    check(solver_stub)

