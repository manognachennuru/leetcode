class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        elif len(prices) == 2:
            return prices[1] - prices[0] if prices[1] > prices[0] else 0
        #else 
        left = 0
        right = 1
        maxprofit = 0
        for right in range(0,len(prices)):
            if prices[right] < prices[left]:
                left = right
            maxprofit = max(prices[right] - prices[left], maxprofit)
        return maxprofit