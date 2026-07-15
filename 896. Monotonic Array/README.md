# 📈 896. Monotonic Array

> **Difficulty:** 🟢 Easy  
> **Problem Link:** https://leetcode.com/problems/monotonic-array/

## 📝 Problem Description

Given an integer array `nums`, determine whether it is **monotonic**.

A monotonic array is one that is either:
- 📈 **Non-decreasing** (each element is greater than or equal to the previous one), or
- 📉 **Non-increasing** (each element is less than or equal to the previous one).

Return `true` if the array is monotonic; otherwise, return `false`.

---

## 💡 Approach

The solution checks whether the original array already matches its sorted versions:

1. Sort the array in **ascending** order and compare it with the original array.
2. Sort the array in **descending** order and compare it with the original array.
3. If either comparison matches, the array is monotonic; otherwise, it is not.

This approach is simple, readable, and leverages Python's built-in sorting functionality.

---

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(n log n)`
  - Sorting the array takes `O(n log n)`. Since two sorted comparisons are performed, the overall complexity remains `O(n log n)`.

- **Space Complexity:** `O(n)`
  - The `sorted()` function creates a new copy of the array.

---

## 🔗 Connect with Me

👨‍💻 **LeetCode Profile:**  
https://leetcode.com/u/filo_mody/

⭐ If you found this solution helpful, feel free to check out my other LeetCode solutions!
