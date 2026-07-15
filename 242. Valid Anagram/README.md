# 🧩 242. Valid Anagram

🔗 **Problem Link:** [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

Given two strings `s` and `t`, determine whether `t` is an anagram of `s` — meaning it uses exactly the same letters, with exactly the same frequencies, just rearranged.

---

## 🧠 My Approach

I used a sort-and-compare strategy, since two strings are anagrams of each other if and only if their sorted character sequences are identical.

- I converted both `s` and `t` into lists of characters with `list(map(str, ...))`.
- I sorted both lists in place with `.sort()`, which arranges each string's letters into the same canonical order.
- I then compared the two sorted lists directly with `!=`. If they differ at all, the strings can't be anagrams, so I return `False`.
- If the sorted lists are equal, every letter and its frequency line up exactly, so I return `True`.
- **Edge case handled:** if `s` and `t` have different lengths, their sorted lists will naturally differ (either in content or length), so the comparison correctly returns `False` without needing an explicit length check.

---

## ⏱️ Time Complexity
**O(n log n)** — sorting each string dominates the runtime, since comparing the two sorted lists afterward only takes O(n).

## 💾 Space Complexity
**O(n)** — converting `s` and `t` into character lists creates two new O(n)-sized structures.

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
