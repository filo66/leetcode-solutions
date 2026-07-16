# 🧩 657. Robot Return to Origin

🔗 **Problem Link:** [Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin/)

Given a sequence of moves (`'R'`, `'L'`, `'U'`, `'D'`) for a robot starting at `(0, 0)`, determine whether it ends up back at the origin.

---

## 🧠 My Approach

I tracked the robot's position with a simple two-element list, `current = [0, 0]`, representing `[x, y]`.

I loop through each character in `moves` and update the coordinates accordingly:
- `'U'` increments the y-coordinate.
- `'D'` decrements the y-coordinate.
- `'R'` increments the x-coordinate.
- Anything else (which, given the problem's valid inputs, can only be `'L'`) decrements the x-coordinate.

Using an `else` for `'L'` instead of an explicit check keeps the branching short since the problem guarantees only these four characters appear. Once every move has been applied, I just compare `current` to `[0, 0]` — if they match, the robot is back at the origin and I return `True`, otherwise `False`.

---

## ⏱️ Time Complexity
**O(n)** — a single pass through `moves`, doing O(1) work per character, where n is the length of `moves`.

## 💾 Space Complexity
**O(1)** — only a fixed-size two-element list is used regardless of input size.

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
