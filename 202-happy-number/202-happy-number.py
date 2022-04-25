class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            current = n
            Sum = 0
            #check sum of squares of n
            while current != 0:
                current,d = divmod(current,10)
                Sum += d**2
                
            if Sum in seen:
                return False
            
            seen.add(Sum)
            n = Sum
        return True