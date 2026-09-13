class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        n = len(prices)
        prefixMin = [0] * n

        prefixMin[0] = prices[0]
        for i in range(1, n):
            prefixMin[i] = min(prefixMin[i - 1], prices[i])
        
        maxProfit = float('-inf')
        for i in range(1, n):
            profit = prices[i] - prefixMin[i]
            maxProfit = max(maxProfit, profit)

        return max(0, maxProfit)
