class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        total = 0
        
        while n > 0:
            n, r = divmod(n,10)
            prod *= r
            total += r
        return prod - total