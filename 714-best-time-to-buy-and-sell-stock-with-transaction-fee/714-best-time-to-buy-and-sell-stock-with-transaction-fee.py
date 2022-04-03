from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #https://leetcode.com/discuss/study-guide/1490172/Dynamic-programming-is-simple
        @lru_cache(None)
        def dp(pos,Bought):
            
            maxprofit = 0
            
            if pos == len(prices):
                return 0
            
            if Bought:
                #selling
                maxprofit = max(maxprofit, dp(pos + 1, False) + prices[pos] - fee)
                
            else:
                #buying
                maxprofit = max(maxprofit, dp(pos + 1, True) - prices[pos])
                
            #doing nothing
            maxprofit = max(maxprofit, dp(pos + 1, Bought))
            
            return maxprofit
            
        return dp(0,False)