class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #https://leetcode.com/discuss/study-guide/1490172/Dynamic-programming-is-simple
        #iterative solution, where we are using a dp table(matrix) , 
        #instead of a dp function 
        
        dp = [[0,0] for _ in range(0,len(prices)+1)]
        for pos in reversed(range(0,len(prices))):
            for Bought in [True, False]:
                maxprofit = 0
            
                if Bought:
                    #selling
                    maxprofit = max(maxprofit, dp[pos + 1][False] + prices[pos] - fee)  
                else:
                    #buying
                    maxprofit = max(maxprofit, dp[pos + 1][True] - prices[pos])
                
                #doing nothing
                maxprofit = max(maxprofit, dp[pos + 1][Bought])
                    
                dp[pos][Bought] = maxprofit
        return dp[0][False]