# Recursion

## Approach

Recursion is a technique where a function calls itself to solve a smaller version of the same problem.

Each recursive problem generally has two important parts:

- Base Case
- Recursive Case

### Problems Covered

1. Factorial
2. Fibonacci
3. Sum of Array
4. Reverse String

---

## Base Case

The base case is the condition that stops the recursive calls.

Without a base case, the function would keep calling itself and eventually cause a recursion error.

Examples:

### Factorial

```python
if n == 0 or n == 1:
    return 1