# 🧩 1822. Sign of the Product of an Array

🔗 **Problem Link:** [Sign of the Product of an Array](https://leetcode.com/problems/sign-of-the-product-of-an-array/)

Given an integer array `nums`, compute the product of all its values and return `1` if the product is positive, `-1` if it's negative, or `0` if it's zero.

---

## 🧠 My Approach

I let Python's `math` module do the heavy lifting instead of manually tracking signs.

- I used `math.prod(nums)` to compute the product of every element in `nums` in one call.
- I then compared that `product` against `0` with simple `if`/`elif`/`else` checks:
  - If `product < 0`, I return `-1`.
  - If `product > 0`, I return `1`.
  - Otherwise (meaning `product == 0`), I return `0`.
- **Edge case handled:** if any element in `nums` is `0`, `math.prod` naturally produces a product of `0`, so the `else` branch correctly returns `0` without needing to explicitly scan for zero elements beforehand.

---

## ⏱️ Time Complexity
**O(n)** — `math.prod` multiplies through all `n` elements once; the final comparisons are O(1).

## 💾 Space Complexity
**O(1)** — only a single `product` value is stored; no extra data structures scale with the input.

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
