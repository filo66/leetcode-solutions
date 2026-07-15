# 🧩 66. Plus One

🔗 **Problem Link:** [Plus One](https://leetcode.com/problems/plus-one/)

Given a large integer represented as an array of digits (most significant digit first), increment the number by one and return the result as a new digit array.

---

## 🧠 My Approach

I sidestepped manual digit-by-digit carrying by converting the whole thing to and from a Python integer.

- I joined all the digits in `digits` into a single string with `"".join(map(str, digits))`, then converted that string into an actual integer `num` using `int(...)`. This reconstructs the full large number from its digit array.
- I incremented `num` by `1` directly, letting Python's built-in arbitrary-precision integer arithmetic handle any carrying — including cases where a `9` rolls over to `10` or a whole sequence of `9`s cascades into a new leading digit.
- I converted `num` back into a string with `str(num)`, then mapped each character back to an `int`, producing the final digit list with `list(map(int, str(num)))`.
- **Edge case handled:** when the input is all `9`s (e.g. `[9]` → `10`, or `[9,9]` → `100`), converting to an integer and back naturally produces the extra leading digit without any special-casing, since Python's integer arithmetic and `str()` conversion handle the extra digit automatically.

---

## ⏱️ Time Complexity
**O(n)** — joining the digits, converting to/from an integer, and mapping back to a list are all linear in the number of digits `n` (Python's big-integer arithmetic for a single increment is effectively linear in the number of digits here).

## 💾 Space Complexity
**O(n)** — the joined string, the integer, and the resulting output list are all proportional to the number of digits.

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
