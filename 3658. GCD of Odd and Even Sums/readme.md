# 🧮 3658. GCD of Odd and Even Sums

🔗 **Problem:** https://leetcode.com/problems/gcd-of-odd-and-even-sums/description/  
👨‍💻 **My Profile:** https://leetcode.com/u/filo_mody/

---

## 💡 Approach

- The sum of the first `n` odd numbers is `n²`.
- The sum of the first `n` even numbers is `n(n + 1)`.

So we need to find:

```text
gcd(n², n(n + 1))
```

Factor out `n`:

```text
gcd(n², n(n + 1))
= n × gcd(n, n + 1)
= n × 1
= n
```

Since `gcd(n, n + 1) = 1`, the answer is always **`n`**.

---


## ⏱️ Complexity

- **Time:** `O(1)` ⚡
- **Space:** `O(1)` 📦
