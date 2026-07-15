# 🧩 283. Move Zeroes

🔗 **Problem Link:** [Move Zeroes](https://leetcode.com/problems/move-zeroes/)

Given an integer array `nums`, move all the `0`s to the end while keeping the relative order of the non-zero elements, and do it in-place without allocating a new array.

---

## 🧠 My Approach

I used an in-place "remove and re-append" technique directly on `nums` as I iterate over it.

- I looped through `nums` with `for i in nums`.
- Whenever the current value `i` is `0`, I called `nums.remove(0)`, which deletes the **first** occurrence of `0` from the list, shifting every element after it one position to the left.
- Right after removing it, I called `nums.append(0)`, which puts that zero back at the very end of the list.
- The net effect of each remove+append pair is that a zero gets pulled out of its original spot and relocated to the end, while everything else shifts left to fill the gap — which is exactly the in-place behavior the problem asks for, since no new array is created.
- I return `nums` at the end, reflecting the array now reordered with all zeros pushed to the back and non-zero elements kept in their original relative order.

---

## ⏱️ Time Complexity
**O(n²)** — each `nums.remove(0)` call is O(n) since it has to shift all subsequent elements left, and this can happen up to O(n) times (once per zero in the array), giving quadratic time in the worst case.

## 💾 Space Complexity
**O(1)** — the array is modified in-place with `remove`/`append`; no additional data structures proportional to the input size are used.

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
