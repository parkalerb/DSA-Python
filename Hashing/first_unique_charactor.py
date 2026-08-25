"""
Problem: First Unique Character in a String

Difficulty: Easy

Description:
Given a string, find the index of the first non-repeating character.
If every character repeats, return -1.

Concept Used:
- Dictionary (HashMap)
- Character Frequency Count

Time Complexity: O(n)
Space Complexity: O(n)
"""


def first_unique_character(text: str) -> int:
    """
    Find the index of the first unique character.

    Args:
        text: Input string.

    Returns:
        Index of the first unique character.
        Returns -1 if no unique character exists.
    """

    frequency = {}

    # Count frequency of each character
    for character in text:
        frequency[character] = frequency.get(character, 0) + 1

    # Find first unique character
    for index, character in enumerate(text):
        if frequency[character] == 1:
            return index

    return -1


def main():
    """Main function."""

    text = "leetcode"

    result = first_unique_character(text)

    print("Input String :", text)
    print("Output Index :", result)

    if result != -1:
        print("First Unique Character :", text[result])
    else:
        print("No unique character found.")


if __name__ == "__main__":
    main()