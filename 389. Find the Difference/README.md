# 🧩 389. Find the Difference

🔗 **Problem Link:** [Find the Difference](https://leetcode.com/problems/find-the-difference/)

String `t` is just string `s` shuffled with one extra letter inserted somewhere. The task is to figure out and return that extra letter.

---

## 🧠 My Approach

I treated this as a character-matching/removal problem using plain lists.

- I converted both `s` and `t` into lists of characters (`s_lst` and `t_lst`) with `list(map(str, ...))`.
- I looped through every character `i` in `t_lst`.
- If that character exists in `s_lst`, I know it's part of the original string, so I remove **one occurrence** of it from `s_lst` — this is important because it keeps the counts in sync even if a letter appears multiple times, rather than just checking membership once.
- The moment I hit a character `i` that is **not** found in `s_lst` anymore (either because it was never in `s`, or all its occurrences have already been "used up" and removed), I know that's the extra letter, so I return it immediately.
- **Edge case handled:** when `s` is empty, `s_lst` is empty from the start, so the very first character checked in `t_lst` won't be found, and it's correctly returned as the answer.

---

## ⏱️ Time Complexity
**O(n²)** — for each of the up to `n` characters in `t`, the `in` check and the `.remove()` call both scan through `s_lst` linearly, giving quadratic behavior overall.

## 💾 Space Complexity
**O(n)** — two extra lists, `s_lst` and `t_lst`, are created to hold the characters of `s` and `t`.

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
