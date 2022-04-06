class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        
        while n != 1:
            result = 0
            #check sum of squares of n
            while n != 0:
                n,d = divmod(n,10)
                result += d**2
            if result in s:
                return False
            s.add(result)
            n = result
        return True