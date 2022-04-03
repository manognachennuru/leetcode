class Solution(object):
    #from solutions
    #when bought = True, we either sell or do nothing
    #when bought = False, we either buy or do nothing
    #the same idea as previous solution, but using a complex but shorter implementation
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash