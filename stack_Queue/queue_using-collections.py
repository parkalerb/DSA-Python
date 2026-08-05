"""
Program: Queue Implementation using collections.deque

Author: Rohan Parkale
Day 023 - Stack & Queue

Concepts Used:
- Queue
- FIFO (First In, First Out)
- collections.deque
"""

from collections import deque


class Queue:
    """Class to implement Queue using deque."""

    def __init__(self):
        """Initialize an empty queue."""
        self.queue = deque()

    def enqueue(self, item):
        """Insert an element into the queue."""
        self.queue.append(item)
        print(f"\n{item} added to the queue.")

    def dequeue(self):
        """Remove the front element from the queue."""

        if self.is_empty():
            print("\nQueue is empty.")
            return

        removed_item = self.queue.popleft()
        print(f"\n{removed_item} removed from the queue.")

    def front(self):
        """Display the front element."""

        if self.is_empty():
            print("\nQueue is empty.")
            return

        print(f"\nFront Element : {self.queue[0]}")

    def is_empty(self):
        """Check whether the queue is empty."""
        return len(self.queue) == 0

    def display(self):
        """Display all queue elements."""

        if self.is_empty():
            print("\nQueue is empty.")
            return

        print("\nCurrent Queue")

        for item in self.queue:
            print(item)


def main():
    """Main Function."""

    queue = Queue()

    while True:

        print("\n========== Queue Menu ==========")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Display")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            value = input("Enter value: ")
            queue.enqueue(value)

        elif choice == "2":

            queue.dequeue()

        elif choice == "3":

            queue.front()

        elif choice == "4":

            queue.display()

        elif choice == "5":

            print("\nThank you!")
            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()