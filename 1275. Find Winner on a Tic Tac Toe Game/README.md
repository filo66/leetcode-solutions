# 🧩 1275. Find Winner on a Tic Tac Toe Game

🔗 **Problem Link:** [Find Winner on a Tic Tac Toe Game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/)

Given a sequence of moves on a 3x3 Tic-Tac-Toe grid (player A goes first with `'X'`, player B second with `'O'`), determine the outcome: return the winner (`"A"` or `"B"`), `"Draw"` if the board fills with no winner, or `"Pending"` if moves remain.

---

## 🧠 My Approach

I used a 3x3 grid initialized with placeholder integers (1-9, laid out in a boustrophedon-like pattern) so that empty cells stay numeric and can be distinguished from filled cells later.

The steps I followed:
1. **Replay the moves** — iterate through `moves` by index. Even indices belong to player `"A"` (moves first), odd indices belong to `"B"`. Each move overwrites the corresponding grid cell with the player's letter.
2. **Check all 8 winning lines** — explicitly compare the three cells in each of the 3 rows, 3 columns, and 2 diagonals. If all three cells in any line match, that value (the winning player's letter) is returned immediately.
3. **Detect a still-numeric cell** — if no line produced a winner, I scan the whole grid looking for any cell that can still successfully convert to `int()`. Since filled cells are overwritten with `"A"`/`"B"` strings, only untouched cells remain as their original integer placeholders. Finding one means squares are still open, so I return `"Pending"`.
4. **Fallback to Draw** — if no winning line exists and no numeric cell is found, the board is completely full with no winner, so I return `"Draw"`.

---

## ⏱️ Time Complexity
**O(m)** — where m is the number of moves; replaying them takes O(m), while checking the 8 fixed win conditions and scanning the fixed 3x3 grid afterward are both O(1) since the board size never changes.

## 💾 Space Complexity
**O(1)** — the grid is always a fixed 3x3 structure, independent of the input size.

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
