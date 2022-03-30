class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rightMax = prices[-1]
        maxprofit = 0
        for i in range(len(prices)-1,-1,-1):
            rightMax = max(rightMax,prices[i])
            maxprofit = max(maxprofit,rightMax - prices[i])
            
        return maxprofit
    
                