# 🧩 1502. Can Make Arithmetic Progression From Sequence

🔗 **Problem Link:** [Can Make Arithmetic Progression From Sequence](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/)

Given an array of numbers, determine whether it can be rearranged so that the difference between every pair of consecutive elements is the same.

---

## 🧠 My Approach

I used sorting to expose the natural ordering an arithmetic progression would have, then checked consecutive differences.

- I sorted `arr` in place with `.sort()`. My reasoning was that for any valid arithmetic progression, the consecutive differences only come out equal when the numbers are arranged in ascending or descending order — any other arrangement would break the constant-difference pattern. Sorting guarantees ascending order, so it's a reliable way to line the numbers up and expose that constant difference if one exists.
- I calculated the expected common difference upfront as `arr[1] - arr[0]`, using the first two elements of the sorted array.
- I then looped through the rest of the array starting at index `1`, and for each position checked whether `arr[i] - arr[i-1]` matches that expected `difference`.
- The moment any consecutive pair doesn't match the expected difference, I return `False` immediately, since that means no arithmetic progression is possible.
- If the loop completes without finding a mismatch, every consecutive gap is equal, so I return `True`.

---

## ⏱️ Time Complexity
**O(n log n)** — sorting the array dominates the runtime; the single pass checking consecutive differences afterward is O(n).

## 💾 Space Complexity
**O(1)** extra space (ignoring the space used by the sort itself) — the array is sorted in-place and only a single `difference` variable is tracked.

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
