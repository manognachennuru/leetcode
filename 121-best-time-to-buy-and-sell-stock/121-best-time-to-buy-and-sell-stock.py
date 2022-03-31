class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #from solutions - checking time taken
        if len(prices) == 0:
            return 0	
        maxprofit = 0
        sofarMin = prices[0]
        for i in range(0,len(prices)):
            if prices[i] > sofarMin:
                maxprofit = max(maxprofit, prices[i] - sofarMin)
            else:
                sofarMin = prices[i]
        return maxprofit