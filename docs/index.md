# LeetCode Python

This repository holds my Python solutions for various LeetCode problems, typically developed and tested within the Visual Studio Code integrated development environment.

# 🧩 Array & Hashing Problems (Category Index)

Welcome to the index for Array and Hashing problems! This section covers foundational concepts like two-pointer techniques, sliding windows, and hash map optimization.

---

### Key Concepts in Array Solutions

* **Two Pointers:** Optimizing algorithms that involve scanning through a list or array.
* **Sliding Window:** Used for problems requiring contiguous subarrays (often for finding max/min length or sum).
* **Hash Maps (Dictionaries):** Essential for $O(1)$ lookup time to improve time complexity from $O(n^2)$ to $O(n)$.

---

## Problem Index

Below is a list of solved problems in this category. Click the **Explanation** link for the approach, or the **Code** link for the pure Python implementation.

| ID | Title | Difficulty | Time Complexity | Links |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Two Sum | Easy | $O(n)$ | [Explanation](two-sum-explanation.md) \| [Code](../../solutions/1_two_sum.py){target=_blank} |
| **2** | Contains Duplicate | Easy | $O(n)$ | [Explanation](contains-duplicate-explanation.md) \| [Code](../../solutions/2_contains_duplicate.py){target=_blank} |
| **3** | Longest Consecutive Sequence | Medium | $O(n)$ | [Explanation](longest-consecutive-sequence.md) \| [Code](../../solutions/3_longest_consecutive_sequence.py){target=_blank} |
| **4** | Valid Anagram | Easy | $O(n \log n)$ or $O(n)$ | [Explanation](valid-anagram.md) \| [Code](../../solutions/4_valid_anagram.py){target=_blank} |
| **5** | Two Sum II (Input array is sorted) | Medium | $O(n)$ | [Explanation](two-sum-ii.md) \| [Code](../../solutions/5_two_sum_ii.py){target=_blank} |

---

## 💡 Quick Link: Two Sum (ID: 1)

> This problem is solved using a Hash Map (dictionary) to store numbers and their indices. By iterating through the array once, we check if the **complement** (`target - current_number`) is already in the map.

### Complexity
* **Time:** $O(n)$ - A single pass over the array.
* **Space:** $O(n)$ - Required space for the hash map in the worst case.



---

## 🔄 Next Steps

Ready for a new category?

* [**Go to Linked Lists Index**](../linked-lists/index.md)
* [**Return to Homepage**](../index.md)