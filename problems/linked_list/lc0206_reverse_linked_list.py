"""
LeetCode 206 - Reverse Linked List
Category: linked_list
Difficulty: Easy

This file stores training data for ACM-style practice.
You can add solve() and input parsing by yourself.
"""

PROBLEM_INFO = {
    "leetcode_id": 206,
    "title": "Reverse Linked List",
    "category": "linked_list",
    "difficulty": "Easy",
    "url": "https://leetcode.com/problems/reverse-linked-list/",
    "summary": "Given the head of a singly linked list, reverse the list and return the new head.",
    "acm_input": [
        "line1: n (node count)",
        "line2: n integers for node values",
    ],
    "acm_output": "one line with reversed values separated by spaces",
}

TEST_CASES = [
    {
        "name": "basic",
        "input": "5\n1 2 3 4 5\n",
        "expected": "5 4 3 2 1\n",
    },
    {
        "name": "single_node",
        "input": "1\n7\n",
        "expected": "7\n",
    },
    {
        "name": "empty_list",
        "input": "0\n\n",
        "expected": "\n",
    },
]

EDGE_CASE_HINTS = [
    "n = 0",
    "n = 1",
    "all values are equal",
]


# TODO: Implement ACM solve() by yourself.
# def solve() -> None:
#     pass


if __name__ == "__main__":
    print(PROBLEM_INFO["title"], "data is ready")
