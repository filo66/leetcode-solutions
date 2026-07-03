# 🔄 Reverse Integer

## 📝 Problem

Given a signed **32-bit integer** `x`, reverse its digits and return the resulting integer.

If reversing the integer causes it to fall outside the signed 32-bit integer range:

**`[-2³¹, 2³¹ - 1]`**

the function should return **`0`** instead.

---

## 💡 Approach

For this solution, I chose a **string-based approach** for its simplicity and readability.

### Steps

* Convert the integer to a string.
* Transform the string into a list of characters.
* Reverse the list.
* Check if the original number is negative by looking for the `-` sign.
* If the number is negative:

  * Remove the minus sign from the reversed list.
  * Place it back at the beginning of the number.
* Join the characters back into a string and convert it to an integer.
* Validate that the result is within the signed 32-bit integer range.
* Return the reversed integer if it's valid; otherwise, return `0`.

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

> Where **n** is the number of digits in the input integer.

---

## ⏳ Time Taken

**17 minutes**

---

## 👨‍💻 LeetCode Profile

🔗 **https://leetcode.com/u/filo_mody/**

---

⭐ Thanks for checking out my solution! Feel free to explore my LeetCode profile to see more of my problem-solving journey.
