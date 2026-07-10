# 🧮 Fraction to Recurring Decimal

## 📌 Problem

**LeetCode 166 - Fraction to Recurring Decimal**

🔗 https://leetcode.com/problems/fraction-to-recurring-decimal/

---

## 💡 Approach

Instead of converting the fraction to a floating-point number (which loses precision for repeating decimals), this solution simulates the **long division** process.

### 🔍 Algorithm

1. Handle the sign of the result.
2. Compute the integer part using integer division (`//`).
3. Compute the initial remainder (`%`).
4. If the remainder is `0`, return the integer result.
5. Otherwise:
   - Store each remainder and the position where it first appeared.
   - Multiply the remainder by `10`.
   - Append the next digit of the decimal part.
   - Compute the new remainder.
6. If a remainder repeats, the digits between its first occurrence and the current position form the repeating sequence.
7. Insert `(` at the first occurrence of the repeated remainder and append `)` at the end.

---

## 🧠 Why It Works

A repeating decimal is caused by **repeating remainders**, not repeating digits.

Example:

```text
1 / 333 = 0.003003003...
```

Remainders during division:

```text
1 → 10 → 100 → 1 → ...
```

Since the remainder `1` appears again, everything generated after its first occurrence repeats.

Result:

```text
0.(003)
```

---

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(n)`
  - `n` is the length of the repeating cycle.

- **Space Complexity:** `O(n)`
  - For storing previously seen remainders.

---

## 👨‍💻 Author

**LeetCode:** https://leetcode.com/u/filo_mody/

⭐ If you found this solution helpful, consider giving the repository a star!
