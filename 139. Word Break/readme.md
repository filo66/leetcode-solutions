# 🚀 139. Word Break

## 📖 Problem
Determine whether a given string `s` can be segmented into a sequence of one or more dictionary words.

- 🔗 **Problem:** https://leetcode.com/problems/word-break/

---

## 💡 Approach
This solution uses **Dynamic Programming (DP)**.

-  `dp[i]` means the substring `s[:i]` can be formed using words from the dictionary.
-  Start with `dp[0] = True` because an empty string is always valid.
-  For every position `i`, check all previous positions `j`.
-  If `dp[j]` is `True` and `s[j:i]` is in the dictionary, then set `dp[i] = True`.

---

## ⚙️ Complexity

- ⏱️ **Time Complexity:** `O(n²)`
- 💾 **Space Complexity:** `O(n)`

---

## 👨‍💻 My LeetCode Profile

🌟 https://leetcode.com/u/filo_mody/
