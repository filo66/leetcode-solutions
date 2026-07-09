# 🧩 Regular Expression Matching

> **Problem:** https://leetcode.com/problems/regular-expression-matching/description/

## 🚀 Approach

My initial plan was to solve this problem using **recursion**, since that's the standard approach for this challenge. However, I remembered learning about Python's **`re`** (Regular Expressions) library during the **CS50P (CS50's Introduction to Programming with Python)** course, so I decided to use it instead.

The solution relies on `re.fullmatch()`, which checks whether the **entire input string** matches the given regular expression pattern.

- ✅ Returns `True` if the whole string matches the pattern.
- ❌ Returns `False` otherwise.

Using `fullmatch()` ensures that the complete string is validated against the pattern rather than matching only a substring.

## ⏱️ Complexity

| Complexity | Value |
|------------|-------|
| **Time** | Typically **O(n)** for simple patterns, but can degrade to exponential time in the worst case due to regex backtracking. |
| **Space** | **O(1)** auxiliary space for the solution (**O(m + n)** including the regex engine's internal memory). |

## 👨‍💻 Author

**LeetCode Profile:** https://leetcode.com/u/filo_mody/
