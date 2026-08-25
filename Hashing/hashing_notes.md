# Hashing Notes

## 📖 Introduction

Hashing is a technique used to store and retrieve data efficiently using **key-value pairs**. It provides very fast searching, insertion, and deletion operations.

In Python, **Dictionary (`dict`)** is the built-in implementation of a HashMap.

Hashing is one of the most important concepts in Data Structures and is widely used in coding interviews.

---

# 🗂️ Dictionary in Python

A dictionary stores data in the form of **key-value pairs**.

### Syntax

```python
student = {
    "id": 101,
    "name": "Rohan",
    "course": "MCA"
}
```

Accessing values

```python
print(student["name"])
```

Output

```
Rohan
```

---

# 🔑 Key-Value Pair

A dictionary consists of:

- Key → Unique identifier
- Value → Data associated with the key

Example

```python
marks = {
    "Math": 90,
    "Science": 95,
    "English": 88
}
```

Here,

- Keys → Math, Science, English
- Values → 90, 95, 88

---

# 🗺️ HashMap Concept

A **HashMap** stores data using a **hash function**, allowing data to be accessed quickly without searching the entire collection.

Instead of checking every element one by one, the HashMap directly locates the required data.

Python Dictionary works internally like a HashMap.

---

# ⚙️ Hash Function

A hash function converts a key into a unique hash value (or index), which determines where the data will be stored.

Example:

```
Key: "apple"

↓

Hash Function

↓

Hash Value

↓

Memory Location
```

This process makes searching much faster.

---

# 💥 Hash Collision

Sometimes two different keys produce the same hash value.

This situation is called a **Hash Collision**.

Example:

```
Key A
   ↓
 Hash Value = 5

Key B
   ↓
 Hash Value = 5
```

Python handles collisions internally, so developers usually don't need to manage them manually.

---

# 📚 Common Dictionary Operations

## Add

```python
student["age"] = 22
```

---

## Access

```python
print(student["name"])
```

---

## Update

```python
student["course"] = "MCA"
```

---

## Delete

```python
del student["age"]
```

---

## Check Key

```python
if "name" in student:
    print("Key Found")
```

---

# ⏱️ Time Complexity

| Operation | Average Complexity |
|-----------|-------------------|
| Search | O(1) |
| Insert | O(1) |
| Update | O(1) |
| Delete | O(1) |

Worst-case complexity can become **O(n)** due to collisions, but Python's dictionary implementation keeps this very rare in practice.

---

# 🌍 Real-World Applications of Hashing

- User Login Systems
- Password Storage
- Phone Contacts
- Dictionaries
- Database Indexing
- Caching
- URL Shorteners
- Shopping Cart
- Compiler Symbol Tables

---

# 💻 Problems Solved Today

### ✅ Two Sum

Concept Used:

- Dictionary
- HashMap
- Fast Lookup

---

### ✅ Valid Anagram

Concept Used:

- Character Frequency
- Dictionary

---

### ✅ First Unique Character

Concept Used:

- Frequency Counting
- Dictionary

---

# 🎯 Interview Questions

## 1. What is Hashing?

Hashing is a technique used to store and retrieve data efficiently using a hash function.

---

## 2. What is a HashMap?

A HashMap stores data as key-value pairs and provides fast lookup, insertion, and deletion.

In Python, the `dict` data structure acts as a HashMap.

---

## 3. Why is Dictionary lookup O(1)?

A dictionary uses a hash function to calculate the memory location of a key, allowing direct access instead of searching sequentially.

---

## 4. What is the difference between List and Dictionary?

| List | Dictionary |
|------|------------|
| Stores values | Stores key-value pairs |
| Access by index | Access by key |
| Searching is O(n) | Searching is O(1) (average) |

---

## 5. What is a Hash Collision?

A collision occurs when two different keys generate the same hash value.

Python automatically handles collisions internally.

---

## 6. When should you use a Dictionary?

Use a dictionary when:

- Fast searching is required
- Key-value mapping is needed
- Frequency counting
- Caching
- Lookup operations

---

# 📝 Summary

Today I learned the fundamentals of **Hashing** and how Python's **Dictionary** works internally as a HashMap.

Key concepts covered:

- Dictionary
- HashMap
- Hash Function
- Hash Collision
- Key-Value Pair
- Time Complexity

I also solved three interview-focused problems using hashing:

- Two Sum
- Valid Anagram
- First Unique Character

These problems strengthened my understanding of how hashing helps optimize searching and lookup operations from **O(n²)** or **O(n)** to **O(1)** average lookup time.