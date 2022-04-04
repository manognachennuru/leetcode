class Solution:
    def hammingWeight(self, n: int) -> int:
        #from discussions
        '''to get last digit, you can do (n & 1) 
        and increment count if that last digit is 1'''
        count = 0
        while n > 0:
            lastbit = n & 1
            count += lastbit #adds either zero or one
            n = n>>1
        return count