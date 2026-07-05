# 🏛️ Roman to Integer

> **LeetCode #13 - Easy**

🔗 **Problem:** https://leetcode.com/problems/roman-to-integer/description/

👤 **My LeetCode Profile:** https://leetcode.com/u/filo_mody/

---

## 📖 Problem Statement

Roman numerals are represented using seven symbols:

| Symbol | Value |
| :----: | ----: |
|    I   |     1 |
|    V   |     5 |
|    X   |    10 |
|    L   |    50 |
|    C   |   100 |
|    D   |   500 |
|    M   |  1000 |

The goal is to convert a valid Roman numeral into its corresponding integer.

---

## 💡 Approach

The solution is based on a simple observation:

* If the current Roman numeral is **smaller** than the next one, it represents a **subtractive** value, so we **subtract** it.
* Otherwise, we **add** its value to the result.

For example:

* `IV` → `1 < 5` → `-1 + 5 = 4`
* `IX` → `1 < 10` → `-1 + 10 = 9`
* `VI` → `5 > 1` → `5 + 1 = 6`

This rule correctly handles all valid Roman numeral combinations.

---

## 🧠 Algorithm

1. Create a dictionary that maps each Roman numeral to its integer value.
2. Initialize the answer to `0`.
3. Iterate through the string:

   * If the current value is less than the next value, subtract it.
   * Otherwise, add it.
4. Return the final answer.

---

## ⏱️ Complexity Analysis

| Complexity | Value    |
| ---------- | -------- |
| 🕒 Time    | **O(n)** |
| 💾 Space   | **O(1)** |

Where **n** is the length of the Roman numeral string.

---

## 🐍 Python Solution

---

## ✅ Examples

| Input     | Output |
| --------- | ------ |
| `III`     | `3`    |
| `LVIII`   | `58`   |
| `MCMXCIV` | `1994` |

---

## 🎯 Key Takeaway

> **If the current Roman numeral is smaller than the next one, subtract it; otherwise, add it.**

This simple rule is enough to correctly convert every valid Roman numeral into its integer representation.

---

### ⭐ Connect with Me

* 👤 **LeetCode:** https://leetcode.com/u/filo_mody/
* 📌 **Problem:** https://leetcode.com/problems/roman-to-integer/description/
