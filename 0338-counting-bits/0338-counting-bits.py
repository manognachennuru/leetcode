class Solution:
    def helper(self, n): 
        #count number of 1's for a given integer
        count = 0
        while n > 0:
            n = n & (n-1)
            count += 1
        return count
        
    def countBits(self, n: int) -> List[int]:
        result = [0]* (n+1)
        for i in range(0, n+1):
            if i % 2 != 0:
                #if odd
                result[i] = result[i-1] + 1
            else:
                result[i] = self.helper(i)
        return result 