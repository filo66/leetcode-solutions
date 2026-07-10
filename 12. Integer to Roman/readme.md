# 🏛️ LeetCode 12 - Integer to Roman

> **Difficulty:** 🟠 Medium  
> **Problem Link:** https://leetcode.com/problems/integer-to-roman/  

---

## 📖 Problem

Given an integer, convert it to its corresponding **Roman numeral** representation.

---

## 💡 Approach

This solution uses a **Greedy Algorithm**.

### 🔹 Idea

1. Store all Roman numeral values (including special cases like `IV`, `IX`, `XL`, etc.) in **descending order**.
2. Iterate through each value.
3. While the current number is greater than or equal to that value:
   - Append the corresponding Roman symbol.
   - Subtract the value from the number.
4. Continue until the number becomes `0`.

Since we always choose the **largest possible Roman value**, the generated numeral is guaranteed to be correct.

---

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(1)` ✅
  - Roman numerals have a fixed maximum length (the input is limited to `1 <= num <= 3999`), so the number of iterations is bounded.

- **Space Complexity:** `O(1)` ✅
  - Only a fixed dictionary and the output string are used.

---

## 🚀 Key Takeaways

- ✔️ Greedy algorithms work perfectly when choosing the largest valid option always leads to the optimal solution.
- ✔️ Including subtractive values (`IV`, `IX`, `XL`, `XC`, `CD`, `CM`) simplifies the implementation.
- ✔️ The solution is concise, efficient, and easy to understand.

---

- 👨‍💻 **My LeetCode Profile:** https://leetcode.com/u/filo_mody/

---

⭐ If you found this solution helpful, consider giving it a star or following my LeetCode profile!
