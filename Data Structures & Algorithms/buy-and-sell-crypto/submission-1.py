class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0

        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            buy = prices[left]
            sell = prices[right]
            profit = sell - buy

            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            
            right += 1
        
        return maxProfit
