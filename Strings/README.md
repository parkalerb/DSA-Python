# 🔤 Strings

## 📖 Overview

This module covers basic string operations in Python, including reversing a string, checking for a palindrome, and counting vowels.

---

# Problem 1: Reverse String

## Problem

Reverse the given string.

### Algorithm

1. Read the input string.
2. Use slicing (`[::-1]`) to reverse it.
3. Display the reversed string.

### Dry Run

Input:

```
Python
```

Output:

```
nohtyP
```

### Time Complexity

**O(n)**

### Space Complexity

**O(n)**

---

# Problem 2: Palindrome String

## Problem

Check whether the given string is a palindrome.

### Algorithm

1. Read the input string.
2. Reverse the string using slicing.
3. Compare the original and reversed strings.
4. Print the result.

### Dry Run

Input:

```
madam
```

Output:

```
The string is a Palindrome.
```

### Time Complexity

**O(n)**

### Space Complexity

**O(n)**

---

# Problem 3: Count Vowels

## Problem

Count the total number of vowels in a string.

### Algorithm

1. Read the input string.
2. Traverse each character.
3. Check if the character is a vowel.
4. Increment the counter.
5. Display the total count.

### Dry Run

Input:

```
OpenAI
```

Output:

```
Number of vowels: 4
```

### Time Complexity

**O(n)**

### Space Complexity

**O(1)**

---

# 📚 Concepts Covered

- Strings
- Indexing
- Slicing
- String Traversal
- Time Complexity

---

# 🎤 Interview Questions

### Is String Immutable in Python?

Yes. Strings are immutable, meaning they cannot be modified after creation. Any modification creates a new string.

---

### What is Slicing?

Slicing is used to extract a portion of a string.

Example:

```python
text = "Python"
print(text[1:4])   # yth
```

---

### What is the Time Complexity of String Traversal?

Traversing a string takes **O(n)** time because each character is visited once.

---

## 📅 Status

✅ Completed

---

## 👨‍💻 Author

Rohan Parkale