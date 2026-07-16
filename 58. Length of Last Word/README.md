# 🧩 58. Length of Last Word

🔗 **Problem Link:** [Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

Given a string made up of words and spaces, return the length of the last word, where a word is a maximal run of non-space characters.

---

## 🧠 My Approach

I kept this one simple by leaning on Python's built-in string splitting. Calling `s.split()` with no arguments splits the string on any whitespace and automatically discards empty strings, so trailing spaces, leading spaces, and multiple spaces between words are all handled for free — no manual trimming or index-walking needed.

Once I have the list of words, the last word is just `[-1]`, and I return its length with `len()`. This naturally covers the edge cases in the problem: strings with trailing spaces (e.g. `"   fly me   to   the moon  "`) still resolve correctly since `split()` ignores the extra whitespace and gives me a clean list of words to index into.

---

## ⏱️ Time Complexity
**O(n)** — `s.split()` scans the entire string once to identify and collect all words, where n is the length of `s`.

## 💾 Space Complexity
**O(n)** — `split()` builds a list containing all the words in the string, which in the worst case (many short words) is proportional to the length of `s`.

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
