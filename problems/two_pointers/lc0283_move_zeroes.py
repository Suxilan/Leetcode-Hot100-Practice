"""
LeetCode 283 - Move Zeroes
Category: two_pointers
Difficulty: Easy

This file stores training data for ACM-style practice.
You can add solve() and input parsing by yourself.
"""

PROBLEM_INFO = {
    "leetcode_id": 283,
    "title": "Move Zeroes",
    "category": "two_pointers",
    "difficulty": "Easy",
    "url": "https://leetcode.com/problems/move-zeroes/",
    "summary": "Move all 0's to the end while keeping the relative order of non-zero elements.",
    "acm_input": [
        "line1: n (array length)",
        "line2: n integers",
    ],
    "acm_output": "one line with transformed array",
}

TEST_CASES = [
    {
        "name": "basic",
        "input": "5\n0 1 0 3 12\n",
        "expected": "1 3 12 0 0\n",
    },
    {
        "name": "all_zero",
        "input": "4\n0 0 0 0\n",
        "expected": "0 0 0 0\n",
    },
    {
        "name": "no_zero",
        "input": "4\n1 2 3 4\n",
        "expected": "1 2 3 4\n",
    },
]

EDGE_CASE_HINTS = [
    "n = 0",
    "all elements are zero",
    "zero appears only at the end",
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
