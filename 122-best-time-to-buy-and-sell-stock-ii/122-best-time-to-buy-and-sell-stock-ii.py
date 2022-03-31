class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initial idea 
        if len(prices) == 0:
            return 0
        right = 1
        profit = 0
        for right in range(1,len(prices)):
            if prices[right] > prices[right - 1]:
                profit +=  prices[right] - prices [right - 1]
                
        return profit
                