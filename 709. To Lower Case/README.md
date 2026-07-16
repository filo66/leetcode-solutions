# 🧩 709. To Lower Case

🔗 **Problem Link:** [To Lower Case](https://leetcode.com/problems/to-lower-case/)

Given a string, return it with every uppercase letter converted to its lowercase equivalent.

---

## 🧠 My Approach

For this one I went straight for Python's built-in `str.lower()` method rather than manually mapping character codes. It handles the conversion for every character in the string in one call — uppercase letters get converted to lowercase, while lowercase letters, digits, and any other characters are left untouched.

This covers all the given cases naturally: a fully uppercase word like `"LOVELY"` becomes `"lovely"`, an already-lowercase word like `"here"` stays the same, and mixed-case input like `"Hello"` is normalized correctly, all without needing to check each character's case explicitly.

---

## ⏱️ Time Complexity
**O(n)** — `lower()` processes each character in the string exactly once, where n is the length of `s`.

## 💾 Space Complexity
**O(n)** — a new string of the same length is created to hold the lowercase result.

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
