# 🧩 1573. Number of Ways to Split a String

🔗 **Problem Link:** [Number of Ways to Split a String](https://leetcode.com/problems/number-of-ways-to-split-a-string/)

Given a binary string, count the number of ways to split it into three non-empty parts so that each part contains the same number of `'1'`s, returning the result modulo `10^9 + 7`.

---

## 🧠 My Approach

I based this on counting `'1'`s and reasoning about where valid cut points can fall, rather than brute-forcing every split.

First, I count the total number of ones (`count1`) in the string. That count immediately tells me a lot:

- **If `count1 == 0`**, every character is `'0'`, so any two distinct cut points among the `len(s) - 1` gaps between characters give a valid split. That's a pure combinatorics case — the number of ways to choose 2 cuts out of those gaps is `(len(s) - 1) * (len(s) - 2) / 2`, which I compute directly and reduce modulo `10^9 + 7`.
- **If `count1` isn't divisible by 3**, it's impossible to split the ones evenly into three parts, so I return `0` immediately.
- **Otherwise**, I collect the index of every `'1'` in the string into a list called `ones`. Each third of the string must contain exactly `count1 // 3` ones, so the boundary between the first and second part can fall anywhere in the gap between the last `'1'` of the first group and the first `'1'` of the second group — and similarly for the boundary between the second and third groups.

  I compute the size of each of those two "flexible gaps":
  - `first` = distance between the last `'1'` of group 1 and the first `'1'` of group 2 (`ones[count1//3] - ones[count1//3 - 1]`)
  - `second` = distance between the last `'1'` of group 2 and the first `'1'` of group 3 (`ones[2*count1//3] - ones[2*count1//3 - 1]`)

  Since the two cut choices are independent, the total number of valid splits is the product `first * second`, reduced modulo `10^9 + 7`.

Edge cases explicitly handled: an all-zero string (unlimited valid splits, computed combinatorially) and a ones-count that doesn't divide evenly by 3 (immediately `0`).

---

## ⏱️ Time Complexity
**O(n)** — a single pass to count and locate the ones, where `n` is the length of the string; everything after that is constant-time index arithmetic.

## 💾 Space Complexity
**O(n)** — the `ones` list can hold up to `n` indices in the worst case (a string of all `'1'`s).

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
