# 💰 1672. Richest Customer Wealth

🔗 **Problem Link:**  
https://leetcode.com/problems/richest-customer-wealth/

## 📝 Problem Description

You are given a 2D array `accounts` where each row represents a customer's bank accounts. Your task is to calculate each customer's total wealth and return the maximum wealth among all customers.

---

## 🧠 My Approach

I iterated through each customer in the `accounts` list and replaced their list of bank balances with the sum of its values, effectively converting each row into the customer's total wealth.

After all rows were converted into total wealth values, I simply returned the largest value using `max()`, which represents the richest customer's wealth.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** 
**O(m × n)** — I sum every bank account balance exactly once, where `m` is the number of customers and `n` is the number of bank accounts per customer.


- **💾 Space Complexity:**
**O(1)** — The input list is modified in place, and only a few extra variables are used.

---

## 👤 Connect

Check out more of my LeetCode solutions here:

🔗 https://leetcode.com/u/filo_mody/

---

## ⭐ Support

If you found this repository helpful, please consider giving it a **⭐ Star**. It helps support my work and motivates me to keep sharing more solutions! 🚀
