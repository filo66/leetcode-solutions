class Solution:
    def numWays(self, s: str) -> int:
        mod = 10**9 + 7

        count1 = s.count("1")

        if count1 == 0:
            return ((len(s) - 1) * (len(s) - 2) // 2) % mod

        if count1 % 3 != 0:
            return 0

        ones = []

        for i, j in enumerate(s):
            if j == "1":
                ones.append(i)

        first = ones[count1 // 3] - ones[count1 // 3 - 1]
        second = ones[2 * count1 // 3] - ones[2 * count1 // 3 - 1]

        return (first * second) % mod
