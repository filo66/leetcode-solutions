# 🚫 1169. Invalid Transactions

## 📝 Problem

Given a list of transactions, identify all **invalid transactions**.

A transaction is considered invalid if:

* 💰 Its amount is greater than **1000**.
* 🌍 There exists another transaction with the **same name**, in a **different city**, within **60 minutes** (inclusive).

🔗 **Problem Link:**
https://leetcode.com/problems/invalid-transactions/?q=1169

---

## 💡 My Approach

* 📌 Parse each transaction by splitting it into:

  * Name
  * Time
  * Amount
  * City
* 🔢 Convert **time** and **amount** to integers for easier comparison.
* 💰 Immediately mark any transaction with an amount greater than **1000** as invalid.
* 🔍 Compare every pair of transactions:

  * Check if they belong to the same person.
  * Check if they were made in different cities.
  * Check if the time difference is at most **60 minutes**.
* ✅ Add every transaction that satisfies the invalid conditions to the final result.

---

## ⏱️ Complexity

* **Time:** `O(n²)`
* **Space:** `O(n)`

---

## 👨‍💻 My LeetCode Profile

🔗 https://leetcode.com/u/filo_mody/
