# 🧩 1768. Merge Strings Alternately

🔗 **Problem Link:** [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/)

Given two strings `word1` and `word2`, merge them by alternating characters starting with `word1`. If one string runs out first, the remaining tail of the longer string is appended at the end.

---

## 🧠 My Approach

I pre-allocated a list `leni` with a length equal to `len(word1) + len(word2)`, since that's exactly the final merged string's length, and filled it in index by index.

- I looped through indices `0` to `len(leni) - 1`.
- On **even** indices, I pulled the next character from `word1` (`word1[0]`) and placed it at that position, then stripped that character off the front of `word1` using `removeprefix`.
- On **odd** indices, I did the same thing but with `word2`.
- **Edge case handling:** once one of the strings runs out of characters, indexing `word1[0]` (or `word2[0]`) raises an `IndexError`. I caught that exception and, in the `except` block, appended whatever remains of the *other* string directly to `leni`, then broke out of the loop — this covers the case where one word is longer than the other and its leftover tail just gets tacked onto the end.
- Finally, I joined `leni` into a single string and returned it.

---

## ⏱️ Time Complexity
**O(n²)** — for every character processed, `word1.removeprefix(word1[0])` (and the equivalent for `word2`) builds a brand new string by copying all remaining characters, so trimming one character at a time across `n` iterations costs O(n) each time, giving O(n²) overall.

## 💾 Space Complexity
**O(n)** — the `leni` list holds one entry per character of the final merged string (length `len(word1) + len(word2)`), plus the shrinking copies of `word1`/`word2` produced by `removeprefix`, which stay within O(n).

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
