# 🧩 String to Integer (atoi)

> **LeetCode #8**  
> https://leetcode.com/problems/string-to-integer-atoi/description/

## 📌 Overview

This problem requires implementing the behavior of the C/C++ `atoi` function.

Although the idea seems straightforward, the challenge lies in handling multiple edge cases correctly, such as:

- Leading whitespace
- Optional `+` or `-` signs
- Invalid characters
- Integer overflow
- Empty or invalid input

---

## 💡 Approach

My solution processes the string in a single pass:

1. Remove any surrounding whitespace.
2. Check for an optional sign (`+` or `-`).
3. Read consecutive digits and build the number.
4. Stop immediately when a non-digit character is encountered.
5. Convert the collected digits into an integer.
6. Clamp the result to the 32-bit signed integer range before returning it.

---

## ⚠️ Challenges Faced

While solving this problem, I ran into several edge cases that caused incorrect answers:

- Handling empty strings after removing whitespace.
- Correctly processing optional `+` and `-` signs.
- Stopping parsing immediately after the first non-digit character.
- Returning `0` when no valid digits are found.
- Clamping values that exceed the 32-bit signed integer range.
- Avoiding parsing digits that appear after an invalid character (e.g., `"0 123"` should return `0`, not `123`).

---

## ⏱️ Complexity

| Complexity | Value |
|------------|:-----:|
| **Time** | **O(n)** |
| **Space** | **O(n)** |

- **Time Complexity:** `O(n)` because the string is traversed at most once.
- **Space Complexity:** `O(n)` due to storing the parsed digits before conversion.

---

## 👨‍💻 Author

- **LeetCode:** https://leetcode.com/u/filo_mody/
