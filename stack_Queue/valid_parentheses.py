"""
Problem: Valid Parentheses

Difficulty: Easy

Description:
Given a string containing only the characters:
(), {}, []

Determine whether the input string is valid.

A string is valid if:
1. Every opening bracket has a matching closing bracket.
2. Brackets are closed in the correct order.

Concept Used:
- Stack

Time Complexity: O(n)
Space Complexity: O(n)
"""


def is_valid_parentheses(text: str) -> bool:
    """
    Check whether the given parentheses string is valid.

    Args:
        text: Input string containing brackets.

    Returns:
        True if the string is valid, otherwise False.
    """

    stack = []

    bracket_pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in text:

        if character in "([{":
            stack.append(character)

        elif character in ")]}":

            if not stack:
                return False

            top = stack.pop()

            if top != bracket_pairs[character]:
                return False

    return len(stack) == 0


def main():
    """Main Function."""

    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}"
    ]

    print("========== Valid Parentheses ==========\n")

    for text in test_cases:

        result = is_valid_parentheses(text)

        print(f"Input  : {text}")
        print(f"Output : {result}")
        print("-" * 35)


if __name__ == "__main__":
    main()