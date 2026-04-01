"""
LeetCode 3 - Longest Substring Without Repeating Characters
Category: sliding_window
Difficulty: Medium

This file stores training data for ACM-style practice.
You can add solve() and input parsing by yourself.
"""

PROBLEM_INFO = {
    "leetcode_id": 3,
    "title": "Longest Substring Without Repeating Characters",
    "category": "sliding_window",
    "difficulty": "Medium",
    "url": "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
    "summary": "Return the length of the longest substring without repeating characters.",
    "acm_input": [
        "line1: string s",
    ],
    "acm_output": "one line with an integer (max length)",
}

TEST_CASES = [
    {
        "name": "example1",
        "input": "abcabcbb\n",
        "expected": "3\n",
    },
    {
        "name": "example2",
        "input": "bbbbb\n",
        "expected": "1\n",
    },
    {
        "name": "example3",
        "input": "pwwkew\n",
        "expected": "3\n",
    },
    {
        "name": "empty",
        "input": "\n",
        "expected": "0\n",
    },
]

EDGE_CASE_HINTS = [
    "empty string",
    "all characters are unique",
    "all characters are the same",
]


def _normalize_output(text: str) -> str:
    # Ignore trailing spaces and final empty lines during comparison.
    lines = [line.rstrip() for line in text.splitlines()]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def check(solver) -> bool:
    """Run built-in test cases against solver(input_str) -> output_str."""
    all_passed = True
    for i, case in enumerate(TEST_CASES, start=1):
        actual = solver(case["input"])
        expected = case["expected"]
        if _normalize_output(actual) != _normalize_output(expected):
            all_passed = False
            print(f"[FAIL] case#{i} {case['name']}")
            print("  input   :", repr(case["input"]))
            print("  expected:", repr(expected))
            print("  actual  :", repr(actual))
        else:
            print(f"[PASS] case#{i} {case['name']}")
    return all_passed


# TODO: Implement ACM solve() by yourself.
# def solve() -> None:
#     pass


# TODO: Replace this stub with your own solver and run check(your_solver).
def solver_stub(_: str) -> str:
    return ""


if __name__ == "__main__":
    print(PROBLEM_INFO["title"], "data is ready")
    print("Run check with your own solver: check(your_solver)")
