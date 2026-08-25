"""
Problem: Two Sum

Difficulty: Easy

Description:
Given an array of integers and a target value, return the indices
of the two numbers such that they add up to the target.

Concept Used:
- HashMap (Dictionary)

Time Complexity: O(n)
Space Complexity: O(n)
"""


def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    Find the indices of two numbers whose sum equals the target.

    Args:
        numbers: List of integers.
        target: Target sum.

    Returns:
        List containing the indices of the two numbers.
        Returns an empty list if no solution exists.
    """

    hashmap = {}

    for index, number in enumerate(numbers):

        complement = target - number

        if complement in hashmap:
            return [hashmap[complement], index]

        hashmap[number] = index

    return []


def main():
    """Main function."""

    numbers = [2, 7, 11, 15]
    target = 9

    result = two_sum(numbers, target)

    print("Numbers :", numbers)
    print("Target  :", target)
    print("Output  :", result)


if __name__ == "__main__":
    main()