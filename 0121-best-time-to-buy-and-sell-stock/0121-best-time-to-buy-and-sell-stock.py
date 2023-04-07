class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for day, price in enumerate(prices):
            if price < lowest: 
                lowest = price
            else:
                profit = max(profit, price - lowest)
        return profit
            
            