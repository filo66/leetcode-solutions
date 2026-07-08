# 🔍 LeetCode 30 - Substring with Concatenation of All Words

## 📌 Problem

Given a string `s` and a list of words `words`, return all starting indices where the concatenation of all words appears exactly once, in any order, and without extra characters.

🔗 **Problem Link:**
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

---

## 💡 My Approach

My idea was to check every possible substring that has the same total length as all the words combined.

### Steps

1.  Calculate the total length of all words.
2.  Iterate through every possible starting index.
3.  Extract a substring with the required length.
4.  Split the substring into equal-sized words.
5.  Check if the extracted words match the given words.
6.  If they match, store the starting index.

---

## 🧠 Problems I Faced

### 🚧 1. I thought the order of words mattered

At first, I joined all the words into one string and searched for that exact string.

**Solution:**
I realized that the words can appear in any order, so I changed my approach to split each candidate substring into words and validate it.

### 🚧 2. String slicing mistakes

I accidentally sliced the original string instead of the current substring, which produced incorrect results.

**Solution:**
I fixed the slicing by always working on the current substring being checked.

### 🚧 3. Debugging the logic

It was difficult to understand why some test cases failed.

**Solution:**
I tested the algorithm step by step and printed intermediate values until I found the indexing mistakes.

---

## ⏱️ Complexity

* **Time Complexity:** `O((N - L + 1) × W)`

  * `N` = Length of `s`
  * `L` = Total length of the concatenated words
  * `W` = Number of words

* **Space Complexity:** `O(W)`

---

## 👨‍💻 Author

**Filo Mody**

🔗 **LeetCode Profile:**
https://leetcode.com/u/filo_mody/

---

⭐ If you found this solution helpful, feel free to check out my other LeetCode solutions!
