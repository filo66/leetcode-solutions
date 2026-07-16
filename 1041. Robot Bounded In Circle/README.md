# 🧩 1041. Robot Bounded In Circle

🔗 **Problem Link:** [Robot Bounded In Circle](https://leetcode.com/problems/robot-bounded-in-circle/)

A robot starts at `(0, 0)` facing north and repeats a sequence of instructions (`'G'` move forward, `'L'` turn left, `'R'` turn right) forever. Determine whether the robot is confined to some circle, i.e. never escapes to infinity.

---

## 🌀 My Approach

I tracked the robot's position `(x, y)` and its facing direction as a vector `(dx, dy)`, starting at `(0, 1)` for north.

The key insight is that instead of simulating the instructions forever, I only need to simulate them **4 times in a row** (`4 * instructions`). This works because:
- If the robot ends up facing north again after one pass, its net displacement per cycle stays the same forever, so it's only bounded if that displacement is `(0, 0)`.
- If the robot ends up facing any other direction after one pass, running it 4 times guarantees it completes a full 360-degree rotation back to north, which cancels out any net drift and brings it back to the origin if a cycle exists at all.

For each character in the quadrupled instruction string:
- `'G'` moves the position by the current direction vector: `x += dx`, `y += dy`.
- `'L'` rotates the direction vector 90° counter-clockwise via `dx, dy = -dy, dx`.
- `'R'` (the `else` branch) rotates it 90° clockwise via `dx, dy = dy, -dx`.

After running through the quadrupled instructions, if the robot lands back at `(0, 0)`, it's confined to a circle, so I return `True`; otherwise `False`.

---

## ⏱️ Time Complexity
**O(n)** — simulating `4 * instructions` is still linear in the length of `instructions`, since 4 is a constant factor.

## 💾 Space Complexity
**O(1)** — only a fixed number of variables (`dx`, `dy`, `x`, `y`) are used regardless of input size (the `4*instructions` string itself scales the input by a constant, not asymptotically).

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
