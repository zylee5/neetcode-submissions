class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0

        minBuy = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            sell = prices[i]
            profit = sell - minBuy
            maxProfit = max(maxProfit, profit)
            minBuy = min(minBuy, sell)
        
        return maxProfit