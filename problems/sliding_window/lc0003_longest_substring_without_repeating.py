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


# TODO: Implement ACM solve() by yourself.
# def solve() -> None:
#     pass


if __name__ == "__main__":
    print(PROBLEM_INFO["title"], "data is ready")
