# 🔍 Longest Substring Without Repeating Characters

![LeetCode](https://img.shields.io/badge/LeetCode-Problem%203-orange)
![Language](https://img.shields.io/badge/Python-3.10-blue)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

---

## 📌 Problem

Given a string `s`, find the length of the longest substring without repeating characters.

### Example:

Input: s = "pwwkew"
Output: 3
Explanation: The longest substring without repeating characters is "wke"


---

## 🧠 My Idea (Original Approach)

I tried to solve the problem by manually building substrings using a list.

### What I did:
- Converted the string into a list of characters
- Built a temporary list (`char_lst`) to store characters one by one
- Whenever I detected a repeated character, I tried to fix it by removing it
- Stored each valid substring inside `avilable_text`
- Finally calculated the maximum length from all stored substrings

---

## ❌ Problem in My Approach

The issue happens when a repeated character appears.

### Example: `"pwwkew"`

At some point:


char_lst = ['p', 'w']


When the next character is `"w"`:

- I detect repetition
- I remove `"w"` from the list

Result becomes:

['p']


Then I continue adding characters again:

['p', 'w']


---

### 🔴 Why this is incorrect

The mistake is:

- I only removed the repeated character itself
- I did NOT properly rebuild the substring from the correct starting position
- Old characters like `'p'` stay in the logic even when they should no longer belong to the valid substring window

This leads to:
- Wrong substring segmentation
- Extra invalid substrings stored in `avilable_text`
- Incorrect final answer in some cases

---

## 💡 What I Learned

The main issue in my solution was misunderstanding how to handle repetition inside a substring.

Instead of only removing the duplicate character, the correct idea is:

- When a duplicate appears, the valid substring must be rebuilt correctly
- The structure must always represent a valid sequence with no duplicates

---

## 🚀 Key Insight

This problem taught me that:

- Manually building substrings is error-prone
- Handling duplicates requires restructuring, not partial removal
- A correct solution must always maintain a valid non-repeating sequence dynamically

---

## 📊 Complexity (My Approach)

- Time Complexity: O(n²) in worst case
- Space Complexity: O(n)
