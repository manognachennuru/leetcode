class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False
    
    def sumOfSquares(self,n):
        Sum = 0
        #check sum of squares of n
        while n != 0:
            n,d = divmod(n,10)
            Sum += d**2
        return Sum
                
            