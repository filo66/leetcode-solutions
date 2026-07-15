# 🧩 28. Find the Index of the First Occurrence in a String

🔗 **Problem Link:** [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

Given `needle` and `haystack`, find the starting index of the first place `needle` appears inside `haystack`, or return `-1` if it never appears.

---

## 🧠 My Approach

I leaned on Python's built-in string operations to keep this simple and direct.

- I first checked whether `needle` is present anywhere in `haystack` using the `in` operator.
- If it is, I used `haystack.index(needle)` to get the index of its **first** occurrence — `.index()` always returns the lowest matching index, which is exactly what the problem asks for.
- If `needle` isn't found at all, I return `-1`.
- **Edge case handled:** since `in` and `.index()` both work correctly even when `needle` matches at index `0` or spans the entire `haystack`, those boundary cases fall out naturally without extra logic.

---

## ⏱️ Time Complexity
**O(n·m)** — in the worst case, substring search compares the `m`-length `needle` against each of the `n` possible starting positions in `haystack`; Python's underlying implementation is optimized but this is the standard worst-case bound for substring matching without a specialized algorithm like KMP.

## 💾 Space Complexity
**O(1)** — no extra data structures are allocated; only the existing strings are read.

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
