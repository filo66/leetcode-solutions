class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordDict = set(wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                word =s[j:i] 
                if dp[j] and word in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]
