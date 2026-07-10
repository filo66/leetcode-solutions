# 🧩 Longest Common Prefix

> **LeetCode #14 - Easy**

🔗 **Problem Link:** https://leetcode.com/problems/longest-common-prefix/

---

## 📖 Problem Overview

Given an array of strings, find the **longest prefix** shared by **every string** in the array.

A **prefix** is a sequence of characters that appears at the beginning of a string.

If the strings have **no common prefix**, return an empty string `""`.

### Example

#### Input
```text
["flower", "flow", "flight"]
```

#### Output
```text
"fl"
```

---

## 💡 My Approach

Instead of comparing characters one by one, I generated **every possible prefix** for each string and counted how many times each prefix appeared.

### Steps

1. Create a dictionary to store every prefix and its frequency.
2. Iterate through every string.
3. Generate all prefixes (including the empty prefix) and count their occurrences.
4. Remove any prefix that doesn't appear in **all** strings.
5. Sort the remaining prefixes by their length in descending order.
6. Return the longest remaining prefix.

A `try/except` block is used to safely handle edge cases (such as a single string), returning the first string when necessary.

---

## ⏱️ Complexity Analysis

- **Time Complexity:** **O(N × M + P log P)**
  - `N` = number of strings
  - `M` = maximum string length
  - `P` = number of unique prefixes

- **Space Complexity:** **O(P)**

Since every possible prefix is stored, the solution uses additional memory compared to the optimal character-by-character approach.

---

## ⏰ Solve Time

**33 minutes 22 seconds** ⏱️

---

## 🚀 LeetCode Profile

Feel free to check out my LeetCode solutions and progress:

🔗 https://leetcode.com/u/filo_mody/

---

### ⭐ If you found this solution helpful, consider giving the repository a star!
