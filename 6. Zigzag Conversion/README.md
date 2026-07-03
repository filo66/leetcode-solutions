# 🚀 Zigzag Conversion

> **LeetCode - Medium**

A clean implementation that determines the destination row for each character before constructing the final zigzag string.

---

# 📖 Problem Description

The string is written in a zigzag pattern across a given number of rows and then read row by row.

For example, the string:

```text
PAYPALISHIRING
```

with `numRows = 3` is arranged as:

```text
P   A   H   N
A P L S I I G
Y   I   R
```

Reading each row from top to bottom produces:

```text
PAHNAPLSIIGYIR
```

Implement the following function:

```python
string convert(string s, int numRows)
```

---

# 📝 Examples

### ✅ Example 1

**Input**

```text
s = "PAYPALISHIRING"
numRows = 3
```

**Output**

```text
PAHNAPLSIIGYIR
```

---

### ✅ Example 2

**Input**

```text
s = "PAYPALISHIRING"
numRows = 4
```

**Output**

```text
PINALSIGYAHRPI
```

**Visualization**

```text
P     I    N
A   L S  I G
Y A   H R
P     I
```

---

### ✅ Example 3

**Input**

```text
s = "A"
numRows = 1
```

**Output**

```text
A
```

---

# 📌 Constraints

- 🔹 `1 <= s.length <= 1000`
- 🔹 `s` consists of uppercase and lowercase English letters, `','`, and `'.'`
- 🔹 `1 <= numRows <= 1000`

---

# 💡 My Approach

Instead of simulating the zigzag pattern directly, I searched for a way to determine **which row each character should belong to**.

I created a helper function called **`ranking()`** that generates a list containing the row number for every character in the string. The function builds the repeating zigzag row order by alternating between moving downward and upward through the rows until every character has been assigned a row.

In the **`convert()`** function, I created a list containing **`numRows`** empty lists. Using the row indices returned by `ranking()`, each character is placed into its corresponding row.

Finally, I concatenate all rows together to produce the required zigzag conversion.

### 🔄 The solution works in two simple steps:

1. 📍 Determine the destination row for every character.
2. 🧩 Group the characters into their rows and concatenate them to build the final answer.

---

# ⚠️ Problem I Faced

While generating the row order inside the **`ranking()`** function, the resulting `rank_lst` sometimes contained **one extra element**.

### ✅ Solution

I fixed the issue by returning only the required number of elements:

```python
return rank_lst[:text_len]
```

This guarantees that the number of row indices always matches the length of the input string.

---

# ⏱️ Complexity Analysis

| Complexity | Value |
|------------|-------|
| 🕒 Time Complexity | **O(n)** |
| 💾 Space Complexity | **O(n)** |

> Where **n** is the length of the input string.

---

# 📊 Submission Information

| 📌 | Information |
|----|-------------|
| 👨‍💻 **LeetCode Profile** | **https://leetcode.com/u/filo_mody/** |
| ⏳ **Time Taken** | **01:47:25** |
| 🎯 **Difficulty** | **Medium** |

---

<div align="center">

### ⭐ If you found this solution helpful, consider giving the repository a star!

**Happy Coding! 🚀**

</div>
