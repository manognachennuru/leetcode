class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #from solutions, 
        '''the buying day will be the last continuous day that the price is smallest. Then, the selling day will be the last continuous day that the price is biggest.'''
        if len(prices) == 0:
            return 0
        sell = 0
        buy = 0
        profit = 0
        i = 0
        while i < len(prices)-1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i = i + 1
            buy = prices[i]
                
            while i < len(prices) - 1 and prices[i] < prices[i + 1]:
                i = i + 1
            sell = prices[i]
            
                
            profit += sell - buy
        return profit
                