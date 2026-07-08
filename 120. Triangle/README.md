# 🔺 Triangle - LeetCode 120

> Find the minimum path sum from the top to the bottom of a triangle.

🔗 **Problem:** https://leetcode.com/problems/triangle/

---

## 💡 My Approach

I solved this problem using **Depth-First Search (DFS)** with **Memoization**.

Starting from the top of the triangle, I recursively explore the two possible moves at each position:

- Stay at the same index in the next row.
- Move to the next index in the next row.

For every state `(row, index)`, I compute the minimum path sum from that position to the bottom. Since the same state can be reached multiple times, I store its result in a **memoization dictionary**. This ensures that each state is calculated only once, significantly improving the performance.

Finally, the answer is the minimum path sum starting from the top of the triangle.

---

## ⏱️ Complexity

- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(n²)`

> Where `n` is the number of rows in the triangle.

---

## 🚀 LeetCode Profile

👤 https://leetcode.com/u/filo_mody/

If you found this explanation helpful, feel free to check out my other LeetCode solutions. ⭐
