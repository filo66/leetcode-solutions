class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        for i in range(len(accounts)):
            accounts[i] = sum(accounts[i])
    
        return max(accounts)
