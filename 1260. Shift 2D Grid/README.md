# 🧩 1260. Shift 2D Grid

🔗 **Problem Link:** [Shift 2D Grid](https://leetcode.com/problems/shift-2d-grid/)

Given an `m x n` grid and an integer `k`, shift every element `k` times, where each shift moves an element one position to the right, wrapping to the start of the next row, and wrapping the very last element back to `grid[0][0]`.

---

## 🧠 My Approach

I treated this as a direct simulation of the shift operation, repeated `k` times.

- For each of the `k` shifts, I first make a copy of the current grid (`copyied_grid`) so I always read from the pre-shift state while writing into the original `grid`.
- I then iterate over every cell `(i, j)` in the grid:
  - If `j` isn't the last column, the value at `(i, j)` moves one step right to `(i, j+1)`.
  - If `j` is the last column but `i` isn't the last row, the value wraps down to the start of the next row, `(i+1, 0)`.
  - If `(i, j)` is the very last cell in the grid, it wraps all the way around to `(0, 0)`.
- Repeating this single-shift logic `k` times in an outer loop naturally handles wraparound across rows and even across the full grid, without needing to compute a flattened index or a modulo shortcut.
- Edge cases like `k` being larger than the total number of cells are handled correctly since each shift is applied independently and consistently — the wraparound logic keeps working no matter how many times it loops around.

---

## ⏱️ Time Complexity
**O(k · m · n)** — for each of the `k` shifts, the code makes a full copy of the grid and does a full `m x n` traversal to move every element one step.

## 💾 Space Complexity
**O(m · n)** — each iteration allocates a new `copyied_grid` that's the same size as the input grid (plus the output grid itself, which is also `m x n`).

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
