# 🚇 Design Underground System

Python solution for **LeetCode 1396 - Design Underground System**.

## 📌 Problem

🔗 https://leetcode.com/problems/design-underground-system/description/

## 💡 Approach

I used two lists:

* **`checkin_lst`** → Stores passengers who have checked in.
* **`final_lst`** → Stores completed trips with their travel times.

When a passenger checks in, their ID, station, and time are saved.

When they check out, the travel time is calculated and added to `final_lst`.

To get the average travel time, the program:

1. Finds all trips between the given stations.
2. Adds their travel times.
3. Returns the average.

## ⏱️ Complexity

* **Check In:** O(n)
* **Check Out:** O(n)
* **Get Average Time:** O(n)

## 🛠️ Language

* 🐍 Python 3

## 👨‍💻 Author

**Filo Mody**

🔗 LeetCode Profile:
https://leetcode.com/u/filo_mody/
