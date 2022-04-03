class Solution(object):
    #https://leetcode.com/discuss/study-guide/1490172/Dynamic-programming-is-simple
    #To further optimize the previous solution, we notice that if we want to calculate the values for pos, we need to calculate only values for pos + 1 and nothing else. Like we don't need values at pos + 2 etc. So we can throw away everything else.
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [0, 0]
        for pos in reversed(range(len(prices))):
            dp_old = dp
            dp = [0, 0]

            for bought in [True, False]:
                max_profit = 0

                if not bought:
                    # Buy stock
                    max_profit = max(max_profit, dp_old[True] - prices[pos] - fee)
                else:
                    # Sell stock
                    max_profit = max(max_profit, dp_old[False] + prices[pos])

                # Do nothing
                max_profit = max(max_profit, dp_old[bought])

                dp[bought] = max_profit
        return dp[False]
