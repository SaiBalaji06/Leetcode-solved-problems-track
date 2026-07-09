class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        pm = []
        mx = prices[n - 1]

        for i in range(n - 1, -1, -1):
            mx = max(mx, prices[i])
            pm.append(mx)

        ans = 0
        for i in range(n):
            if pm[n - i - 1] > prices[i]:
                ans = max(ans, abs(pm[n - i - 1] - prices[i]))

        return ans

        