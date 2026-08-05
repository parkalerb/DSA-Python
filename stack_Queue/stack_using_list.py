"""
Program: Stack Implementation using Python List

Author: Rohan Parkale
Day 023 - Stack & Queue

Concepts Used:
- Stack
- LIFO (Last In, First Out)
- List
"""


class Stack:
    """Class to implement Stack using Python List."""

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, item):
        """Add an element to the top of the stack."""
        self.stack.append(item)
        print(f"\n{item} pushed into the stack.")

    def pop(self):
        """Remove the top element from the stack."""

        if self.is_empty():
            print("\nStack is empty.")
            return

        removed_item = self.stack.pop()
        print(f"\n{removed_item} popped from the stack.")

    def peek(self):
        """Display the top element."""

        if self.is_empty():
            print("\nStack is empty.")
            return

        print(f"\nTop Element : {self.stack[-1]}")

    def is_empty(self):
        """Check whether the stack is empty."""
        return len(self.stack) == 0

    def display(self):
        """Display all elements in the stack."""

        if self.is_empty():
            print("\nStack is empty.")
            return

        print("\nCurrent Stack")

        for item in reversed(self.stack):
            print(item)


def main():
    """Main Function."""

    stack = Stack()

    while True:

        print("\n========== Stack Menu ==========")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            value = input("Enter value: ")
            stack.push(value)

        elif choice == "2":

            stack.pop()

        elif choice == "3":

            stack.peek()

        elif choice == "4":

            stack.display()

        elif choice == "5":

            print("\nThank you!")
            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()