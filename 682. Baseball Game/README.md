# 🧩 682. Baseball Game

🔗 **Problem Link:** [Baseball Game](https://leetcode.com/problems/baseball-game/)

Given a list of operations representing a baseball game's scoring record (numbers, `'+'`, `'D'`, or `'C'`), return the sum of all scores left on the record after applying every operation.

---

## 🧠 My Approach

I used a stack (a plain Python list called `record`) to simulate the scoring record, since every operation only ever depends on the top one or two scores — a classic stack pattern.

I loop through `operations` and try to convert each entry to an integer:
- If it converts successfully, it's a plain score, so I push it onto `record`.
- If the conversion fails (it's not a number), I fall into the `except` block and check which symbol it is:
  - `'+'` — push the sum of the top two scores (guarded with `len(record) >= 2` before adding).
  - `'D'` — push double the top score.
  - `'C'` — pop the top score off, invalidating it.

Using `try/except int()` conveniently distinguishes numeric operations from symbolic ones without needing extra string-parsing logic for negative numbers. At the end, I just return `sum(record)`, which reflects whatever scores are still valid on the stack.

---

## ⏱️ Time Complexity
**O(n)** — each operation in `operations` is processed once with O(1) work (push, pop, or sum of top elements), where n is the number of operations.

## 💾 Space Complexity
**O(n)** — the `record` stack holds at most one entry per operation in the worst case (no `'C'` operations).

---

## 👤 Connect

More solutions and write-ups on my LeetCode profile:
🔗 [https://leetcode.com/u/filo_mody/](https://leetcode.com/u/filo_mody/)

---

⭐ **If this helped you, consider giving it a star!** ⭐
