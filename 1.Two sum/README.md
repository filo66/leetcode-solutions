# 🚀 1.Two Sum - LeetCode Solution

## 📌 Problem
Solve the **Two Sum** problem from LeetCode by returning the indices of the two numbers whose sum equals the given target.

---

# 🧠 My Thought Process

## 1️⃣ Understanding the Constraints

Before writing any code, I started by reading and understanding the **constraints** of the problem to know what inputs were allowed and what the function should return.

---

## 2️⃣ My First Idea

My first approach was a **brute-force solution**.

- Create a loop for the first number.
- Create another loop inside it for the second number.
- Check if:

```python
i + j == target
```

If the condition was true, I would return the indices of both numbers using `.index()`.

---

## ❌ The Problem

Everything looked fine until I tested this case:

```python
nums = [3, 3]
target = 6
```

The output became:

```python
[0, 0]
```

instead of

```python
[0, 1]
```

### 🤔 Why?

Because:

```python
nums.index(3)
```

always returns the **first occurrence** of `3`, which is index `0`.

So even when the second `3` was found, `.index()` still returned `0`.

---

## 💡 My First Fix

To solve this, I decided to use **`enumerate()`**.

Instead of relying on `.index()`, `enumerate()` gives both:

- the current index
- the current value

This allowed me to get the **exact index** of every element, even if there were duplicate values.

---

## ⚠️ Another Problem Appeared

I was using the `remove()` function to temporarily remove the first number from the list so that it wouldn't add itself.

However, this caused issues because modifying the list changed its contents and made tracking indices more complicated.

---

## ✅ Final Solution

Instead of removing elements from the list, I simply made sure the two numbers were **not the same element**.

I updated the condition to:

```python
if i + j == target and index1 != index2:
```

This guarantees that:

- ✅ The sum equals the target.
- ✅ The two indices are different.
- ✅ Duplicate values like `[3, 3]` work correctly.

---

# 🎉 Result

After making this change, the solution worked perfectly for all the test cases, including:

```python
nums = [3, 3]
target = 6
```

Output:

```python
[0, 1]
```

---

# 📚 What I Learned

✨ Always read the constraints first.

✨ `.index()` is not suitable when duplicate values exist.

✨ `enumerate()` is a great way to access both the value and its exact index.

✨ Avoid modifying the list (`remove()`) while searching when indices matter.

✨ Sometimes the simplest fix is just making sure you're not using the same element twice:

```python
index1 != index2
```

---


> ⭐ This solution helped me better understand how duplicate values affect indexing and why `enumerate()` is often a better choice than `.index()` when working with lists.
