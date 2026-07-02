# 🧩 Longest Palindromic Substring

## 📌 Problem

Given a string `s`, return the **longest palindromic substring**.

A palindrome is a string that reads the same forwards and backwards.

---

# 💡 My Approach

I decided to solve this problem using a **brute-force approach** to better understand how palindromes work before learning more advanced algorithms.

### Steps:

1. 🔹 Iterate through every character in the string.
2. 🔹 Build a substring by adding one character at a time.
3. 🔹 Check whether the current substring is a palindrome.
4. 🔹 If it is longer than the current longest palindrome, update the answer.
5. 🔹 Continue until every possible starting position has been checked.

Although this approach is not the most efficient, it helped me understand the problem and practice algorithm analysis.

---

# 🚧 Challenges I Faced

## ❌ 1. Returning the Wrong Answer

Initially, I stored every palindrome inside a list and returned:

```python
max(longest_lst)
```

I later discovered that `max()` compares strings **alphabetically (lexicographically)** instead of comparing their lengths.

For example:

```text
"d" > "bab"
```

So my program returned `"d"` instead of `"bab"`.

### ✅ Solution

Instead of storing every palindrome, I kept track of only the longest palindrome found so far.

---

## ⏱️ 2. Time Limit Exceeded (TLE)

Even though my solution produced the correct answers, LeetCode returned:

> **Time Limit Exceeded**

After analyzing my code, I realized that I was checking far too many substrings.

For every starting position, I generated multiple substrings and checked each one to see if it was a palindrome.

This caused the algorithm to perform a huge number of repeated operations on large inputs.

---

## 🧠 3. Understanding Time Complexity

One of the biggest lessons from this problem was learning that **a correct solution isn't always an accepted solution**.

Even if the logic is correct, an inefficient algorithm can exceed the execution time allowed by LeetCode.

---

# 📊 Time Complexity

Let **n** be the length of the string.

* 🔹 Outer loop → **O(n)**
* 🔹 Inner loop → **O(n)**
* 🔹 Palindrome check → **O(n)**

### Overall Time Complexity

```text
O(n³)
```

### Space Complexity

```text
O(n)
```

---


# ⏳ Time Taken

**🕒 2 Hours 15 Minutes**

---

# 💻 LeetCode Profile

**👤 filo_mody:**

🔗 https://leetcode.com/u/filo_mody/
