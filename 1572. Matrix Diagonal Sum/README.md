# 🧩 1572. Matrix Diagonal Sum

🔗 **Problem Link:** [Matrix Diagonal Sum](https://leetcode.com/problems/matrix-diagonal-sum/)

Given a square matrix, return the sum of its primary diagonal and its secondary diagonal, making sure not to double-count the center element when the matrix has odd dimensions.

---

## 🧠 My Approach

I used a single pass over the rows with two column pointers moving in opposite directions — `x` starting at `0` and incrementing forward for the primary diagonal, and `y` starting at `-1` and decrementing for the secondary diagonal (using negative indexing to grab it from the end of each row).

For every row `i`, I add `i[x]` for the primary diagonal element. Then I check whether the secondary diagonal position actually differs from the primary one before adding `i[y]` — this is the `len(i) + y != x` condition. Since `y` is negative, `len(i) + y` converts it to its equivalent positive index, so comparing it against `x` tells me whether the two diagonals intersect at that row. If they do (which only happens at the center row of an odd-sized matrix), I skip adding it again so `mat[1][1]`-style center elements aren't counted twice.

After processing each row, I move `x` one step right and `y` one step left, and continue until every row has been visited, accumulating the running total in `sum`.

Edge case handled: single-element matrices (e.g. `[[5]]`) and odd-sized matrices where the primary and secondary diagonals meet at the center — the equality check naturally prevents double-counting there.

---

## ⏱️ Time Complexity
**O(n)** — one pass through the `n` rows of the matrix, with constant-time work (two index lookups) per row.

## 💾 Space Complexity
**O(1)** — only a fixed number of scalar variables (`x`, `y`, `sum`) are used regardless of matrix size.

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
