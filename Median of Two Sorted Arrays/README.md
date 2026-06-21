
# Median of Two Sorted Arrays 🚀

![LeetCode](https://img.shields.io/badge/LeetCode-Problem%204-orange)
![Language](https://img.shields.io/badge/Python-3.10-blue)
![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## 📝 Problem

Given two sorted arrays `nums1` and `nums2`, return the median of the two sorted arrays.

### Example 1

```text
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
````

### Example 2

```text
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
```

---

## 💡 How I Thought About the Solution

At the beginning, I wasn't completely sure how the **Median** works, especially when finding its position in an array.

So I searched on YouTube for a simple explanation and found a great video from **The Organic Chemistry Tutor**. The explanation was very clear and helped me understand how to calculate the median index.

🎥 Video:

https://www.youtube.com/watch?v=xkDrB6LQFP0

After understanding the formula from the video, I applied the same idea in my solution.

### 🔍 My Logic

* First, I merged the two arrays into a single list.
* Then I sorted the merged list.
* If the total number of elements is **odd**, I calculate the median index using the formula from the video and subtract **1** because Python uses **zero-based indexing**.
* If the total number of elements is **even**, I find the two middle elements and return their average.

### 📋 Steps

1. Merge both arrays.
2. Sort the merged array.
3. Check if the length is odd or even.
4. Return the middle element if odd.
5. Return the average of the two middle elements if even.

---

## ⏱️ Complexity Analysis

### Time Complexity

```text
O((m + n) log(m + n))
```

📌 Because the merged array is sorted after combining both arrays.

### Space Complexity

```text
O(m + n)
```

📌 Because a new array is created to store all elements from both input arrays.

---

## 🎯 Notes

* ✅ Accepted on LeetCode.
* ✅ Easy to understand and implement.
* ⚠️ This solution does **not** meet the required `O(log(m+n))` complexity mentioned in the problem statement because it relies on sorting.
* 📚 It was a great exercise for understanding how the median works before learning the optimal Binary Search solution.

---

⭐ If you found this repository useful, feel free to give it a star!

```
```
