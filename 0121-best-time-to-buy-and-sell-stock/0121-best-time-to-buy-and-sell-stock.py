class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #use 2 pointers
        if len(prices) == 1:
            return 0
        l = 0
        r = 1
        maxprofit, profit = 0, 0
        
        while r < len(prices):
            #profitable ? 
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxprofit = max(profit, maxprofit)
            else:
                l = r
            r += 1
        return maxprofit
            
        