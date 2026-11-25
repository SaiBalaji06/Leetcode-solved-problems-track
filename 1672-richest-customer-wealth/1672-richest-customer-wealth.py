class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0
        for cust in accounts:
            richest = max(richest, sum(cust))
        
        return richest

        