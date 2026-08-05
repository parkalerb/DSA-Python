# Stack & Queue Notes

## 📖 Introduction

Stack and Queue are two of the most fundamental linear data structures used in Computer Science. They are widely used in software development, operating systems, compilers, web browsers, and many real-world applications.

The main difference between them is the order in which data is inserted and removed.

---

# 📚 Stack

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle.

The last element inserted into the stack is the first one to be removed.

### Example

```
Push 10
Push 20
Push 30

Stack

30  ← Top
20
10
```

If we perform **Pop**, the output will be:

```
30
```

---

# 🔧 Stack Operations

## Push

Adds an element to the top of the stack.

```python
stack.append(10)
```

---

## Pop

Removes the top element.

```python
stack.pop()
```

---

## Peek

Displays the top element without removing it.

```python
stack[-1]
```

---

## is_empty

Checks whether the stack is empty.

```python
len(stack) == 0
```

---

# ⏱️ Stack Complexity

| Operation | Complexity |
|-----------|------------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| Search | O(n) |

---

# 🌍 Stack Applications

- Function Call Stack
- Undo / Redo
- Browser Back Button
- Expression Evaluation
- Parentheses Matching
- Depth First Search (DFS)
- Syntax Parsing

---

# 📚 Queue

A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle.

The first element inserted into the queue is the first one removed.

### Example

```
Enqueue 10
Enqueue 20
Enqueue 30

Front

10 → 20 → 30
```

If we perform **Dequeue**, the output will be:

```
10
```

---

# 🔧 Queue Operations

## Enqueue

Adds an element to the rear of the queue.

```python
queue.append(10)
```

---

## Dequeue

Removes the front element.

```python
queue.popleft()
```

---

## Front

Displays the first element.

```python
queue[0]
```

---

## is_empty

Checks whether the queue is empty.

```python
len(queue) == 0
```

---

# ⏱️ Queue Complexity

| Operation | Complexity |
|-----------|------------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Front | O(1) |
| Search | O(n) |

---

# 🚀 Why use deque?

Python's `collections.deque` is specifically designed for efficient insertion and deletion from both ends.

Advantages:

- Fast Enqueue
- Fast Dequeue
- Better performance than Python List for Queue implementation

---

# 📊 Stack vs Queue

| Stack | Queue |
|--------|--------|
| LIFO | FIFO |
| Insert at Top | Insert at Rear |
| Remove from Top | Remove from Front |
| Push | Enqueue |
| Pop | Dequeue |
| Used in DFS | Used in BFS |

---

# 🌍 Real-World Applications

## Stack

- Browser Back Button
- Undo / Redo
- Function Calls
- Expression Evaluation
- Parentheses Matching
- DFS Algorithm

---

## Queue

- Printer Queue
- CPU Scheduling
- Ticket Booking System
- Customer Support Queue
- BFS Algorithm
- Task Scheduling

---

# 💻 Problems Solved Today

## ✅ Valid Parentheses

Concepts Used:

- Stack
- Push
- Pop
- Matching Brackets

---

## ✅ Stack using List

Concepts Used:

- Python List
- Push
- Pop
- Peek
- LIFO

---

## ✅ Queue using collections.deque

Concepts Used:

- deque
- FIFO
- Enqueue
- Dequeue

---

# 🎯 Interview Questions

## 1. What is a Stack?

A Stack is a linear data structure that follows the **LIFO (Last In, First Out)** principle.

---

## 2. What is a Queue?

A Queue is a linear data structure that follows the **FIFO (First In, First Out)** principle.

---

## 3. Difference between Stack and Queue?

| Stack | Queue |
|--------|--------|
| LIFO | FIFO |
| Push | Enqueue |
| Pop | Dequeue |
| One End | Two Ends |

---

## 4. Why is Stack called LIFO?

Because the last element inserted is the first one removed.

---

## 5. Why is Queue called FIFO?

Because the first element inserted is the first one removed.

---

## 6. Why use deque instead of List?

`deque` provides **O(1)** insertion and deletion from both ends, while removing the first element from a Python List takes **O(n)** time.

---

## 7. What are the applications of Stack?

- Undo / Redo
- Browser History
- DFS
- Parentheses Matching
- Function Calls

---

## 8. What are the applications of Queue?

- CPU Scheduling
- Printer Queue
- BFS
- Customer Service
- Task Scheduling

---

# 📝 Summary

Today I learned two important linear data structures: **Stack** and **Queue**.

### Key Concepts Covered

- Stack
- Queue
- LIFO
- FIFO
- Push
- Pop
- Enqueue
- Dequeue
- Peek
- Front
- Time Complexity

I also implemented three practical programs:

- Valid Parentheses
- Stack using Python List
- Queue using collections.deque

These concepts form the foundation for many advanced algorithms and are frequently asked in technical interviews.