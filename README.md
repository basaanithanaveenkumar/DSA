# Data Structures and Algorithms Repository

This repository contains my solutions to various Data Structures and Algorithms (DSA) problems, organized by topic. Each folder contains implementations and problem solutions related to specific DSA concepts.



# 🚀 Interview Preparation Guide 🚀

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

A structured roadmap to master coding interview topics, algorithms, and data structures.

---

## 📚 Table of Contents
- [Python Data Structures](#-python-data-structures)
- [Roadmaps](#-roadmaps)
- [Time & Space Complexity](#-time--space-complexity)
- [Core Topics](#-core-topics)
- [Algorithms & Techniques](#-algorithms--techniques)
- [Sparsely Asked Topics](#-sparsely-asked-topics)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🐍 Python Data Structures

| Data Structure | Key Methods & Resources |
|----------------|-------------------------|
| **List**       | `append()`, `insert()`, `pop()`, slicing |
| **Dict**       | `get()`, `items()`, `keys()`, `update()` |
| **[Set](https://www.w3schools.com/Python/python_ref_set.asp)** | `add()`, `union()`, `intersection()`, `difference()` |
| **Tuple**      | Immutable, `count()`, `index()` |
| **Deque**      | `popleft()`, `appendleft()` (from `collections`) |
| **Heapq**      | `heappush()`, `heappop()`, `heapify()` |


# [Methods of python (Ex: set)](https://www.w3schools.com/Python/python_ref_set.asp)

---

## 🗺️ Roadmaps
- **[InterviewBit Company-Wise](https://www.interviewbit.com)**: Practice company-specific questions.
- **[Neetcode.io](https://neetcode.io/roadmap)**: Structured problem-solving roadmap.

---

## ⏳ Time & Space Complexity
- **Big O Notation**: Analyze worst-case complexity for algorithms.
- **Tips**: Focus on nested loops (O(n²)), recursion (O(2ⁿ))
- **Time complexity**: Analyze worst-case Time complexity for algorithms.
- **Space complexity**: Analyze worst-case space complexity for algorithms.

---

## 🎯 Core Topics

### � Dynamic Programming
- **Memoization**: Cache results to avoid recomputation.
- **Tabulation**: Build solutions iteratively using tables.
- **0/1 Knapsack**: Maximize value with weight constraints.
- **Longest Common Subsequence**: Find sequences in strings/arrays.

### 🔍 [Binary Search](https://www.youtube.com/watch?v=9nmrkG6QtpQ&list=WL&index=2&ab_channel=GregHogg)
- **Traditional Binarysearch**
- **Condition-Based**: Split search space using custom conditions.
- **Binary Search Tree**: Validate, insert, delete nodes (O(log n)).

### 🌳 Tree
- **DFS** (Pre/In/Post Order): 
  - Iterative & Recursive implementations.
- **BFS** (Level Order): 
  - Use queues for traversal.
  - Handle skewed trees (AVL/Red-Black Trees for balancing).

### 🕸️ Graphs
- **Multi-Source BFS**: Solve problems with multiple starting points.
- **Shortest Path**: Dijkstra (no negative weights), Bellman-Ford (negative weights).

### [Stack (FIFO)](https://www.geeksforgeeks.org/monotonic-stack-in-python/)
- [**Monotonic stack**](https://www.youtube.com/watch?v=e7XQLtOQM3I&ab_channel=takeUforward)
- **linked list stack**: stack data structure using Linked list (dynamic size and push and pop operations O(1))

### Queue (LIFO)
- **BFS of trees and graph**



### 🔗 Linked List
- **Reverse In-Place**: Use iterative pointers or recursion.
- **Inplace reversal of linkedlist**

### 📊 [Sliding Window](https://www.youtube.com/watch?v=GaXwHThEgGk&list=WL&index=1&ab_channel=GregHogg)
- **Fixed/ Variable Length**: Optimize subarray/substring problems.

### 🏗️ Heaps & Priority Queues
- **Top K Elements**: Use min-heap (keep smallest K) or max-heap (negation of values, convert the positive integer to negative integer and negative integer to positive integer).

---

## ⚙️ Algorithms & Techniques
- **Two Pointers**: start LP at begining , RP at the end of array_index
- [**Kadanes algorithm**](https://www.youtube.com/watch?v=hLPkqd60-28&ab_channel=GregHogg)
- **Fast and slow Pointers**
- **Greedy**: Fractional knapsack, activity selection.
- [**Recursion & Backtracking**](https://www.youtube.com/watch?v=L0NxT2i-LOY&t=196s&ab_channel=GregHogg): Permutations, subsets, N-Queens.
- **Prefix Sum**: Subarray sum problems.
- **Monotonic Stack**: Next greater element, Next smaller element histogram area.
- **shortest path**: dijkstra algorithm, Bellman Ford, Floyd warshall

---

## 🌌 Sparsely Asked Topics
- **Tries**: Prefix-based string operations.
- **Topological Sort**: Dependency resolution (DAGs).
- **Divide & Conquer**: Merge/Quick sort
- **Bit Manipulation**: XOR tricks, (silicon companies ask these pattern)
- **Union-Find**: Detect cycles, connected components.
- **Permuatation** : [video](https://www.youtube.com/watch?v=gDGw0cvFXPQ&ab_channel=KunalKushwaha) places of elements can be interchanged. [geeksforgeeks read](https://www.geeksforgeeks.org/permutations-and-combinations/#permutation)

## union find in graphs
---

## 🤝 Contributing
Feel free to submit PRs for corrections, additional resources, or examples!

---

## 📜 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.




























































## Folder Structure

### 📁 [LinkedList](/LinkedList/)
- Implementation of linked list data structure
- Solutions to linked list problems
- Common operations and algorithms
- Created: Apr 30, 2025

### 📁 [arrays](/arrays/)
- Array manipulation problems
- Sorting and searching algorithms
- Matrix operations
- Sliding window techniques
- Created: Apr 30, 2025

### 📁 [bit_manipulation](/bit_manipulation/)
- Problems solved using bitwise operations
- Common bit manipulation techniques
- Bitmask patterns
- Created: Apr 30, 2025

### 📁 [trees](/trees/)
- Binary tree implementations
- Tree traversal algorithms (BFS, DFS)
- BST operations
- Balanced tree problems
- Created: Apr 30, 2025

## How to Use This Repository

1. Navigate to the topic folder you're interested in
2. Each problem solution includes:
   - Problem statement
   - Solution approach
   - Implementation in your preferred language
   - Time and space complexity analysis

## Contribution Guidelines

Contributions are welcome! Please follow these guidelines:
- Add clear problem statements
- Include comments explaining your approach
- Maintain consistent coding style
- Update this README when adding new categories

## Resources
### I would like to give the complete credit to the resources I have followed
- [takeuforward](https://takeuforward.org/plus?source=youtube)
- [GregHog](https://www.youtube.com/watch?v=fvyqbtmor9U&list=PLKYEe2WisBTH48RzVCL_LQrGW-ahPY44S&index=7&ab_channel=GregHogg/)
- [GeeksforGeeks](https://www.geeksforgeeks.org/)
- [LeetCode](https://leetcode.com/)
- [Codeforces](https://codeforces.com/)
- [HackerRank](https://www.hackerrank.com/domains/tutorials/10-days-of-algorithms)
- [small set of questions to practice](https://www.linkedin.com/feed/update/urn:li:activity:7328667967079034880/)
- [small-set-2 from linked in](https://www.linkedin.com/posts/madhanvadlamudi_leetcode-dsa-problemsolving-activity-7329540054727458817-FWRC?utm_source=share&utm_medium=member_desktop&rcm=ACoAACQXQ4QBqLfzuvb2q_NwRd8JuUkBVTumfIk)

Happy coding! 🚀
