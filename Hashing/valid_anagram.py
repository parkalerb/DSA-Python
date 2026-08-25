"""
Problem: Valid Anagram

Difficulty: Easy

Description:
Given two strings, determine whether one string is an anagram
of the other.

An anagram is a word formed by rearranging the letters of
another word using all the original letters exactly once.

Concept Used:
- Dictionary (HashMap)
- Character Frequency Count

Time Complexity: O(n)
Space Complexity: O(n)
"""


def is_anagram(first: str, second: str) -> bool:
    """
    Check whether two strings are anagrams.

    Args:
        first: First input string.
        second: Second input string.

    Returns:
        True if both strings are anagrams, otherwise False.
    """

    if len(first) != len(second):
        return False

    frequency = {}

    # Count characters from the first string
    for character in first:
        frequency[character] = frequency.get(character, 0) + 1

    # Remove characters using the second string
    for character in second:

        if character not in frequency:
            return False

        frequency[character] -= 1

        if frequency[character] == 0:
            del frequency[character]

    return len(frequency) == 0


def main():
    """Main function."""

    first = "listen"
    second = "silent"

    result = is_anagram(first, second)

    print("First String  :", first)
    print("Second String :", second)
    print("Is Anagram?   :", result)


if __name__ == "__main__":
    main()