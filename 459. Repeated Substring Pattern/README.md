# 🧩 459. Repeated Substring Pattern

🔗 **Problem Link:** [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)

Given a string `s`, determine whether it can be built by repeating some substring of itself multiple times back to back.

---

## 🧠 My Approach

I used a brute-force candidate-length search over possible substring sizes.

- I got `n`, the length of `s`, and looped `length` from `1` up to `n // 2` (inclusive), since a repeating unit can never be longer than half the string — otherwise it couldn't repeat at least twice.
- For each candidate `length`, I first checked `n % length == 0`. This is a necessary condition: if `length` doesn't evenly divide `n`, repeating a substring of that size can never exactly reconstruct `s`, so there's no point testing it further.
- If it divides evenly, I built a candidate string by repeating the first `length` characters (`s[:length]`) exactly `n // length` times, and compared it directly against `s`. If they match, `s` is indeed made up of repeated copies of that substring, so I return `True` immediately.
- If no candidate length works by the end of the loop, I return `False`.
- **Edge case handled:** for a string with no valid repeating substring shorter than itself (like `"aba"`), every candidate length either fails the divisibility check or fails the reconstruction check, so the loop naturally falls through to `False`.

---

## ⏱️ Time Complexity
**O(n²)** — in the worst case there are up to O(n) candidate lengths to try, and for each valid one, building and comparing the repeated string takes O(n), giving quadratic time overall.

## 💾 Space Complexity
**O(n)** — each candidate reconstruction (`s[:length] * (n // length)`) builds a new string of length `n`.

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
