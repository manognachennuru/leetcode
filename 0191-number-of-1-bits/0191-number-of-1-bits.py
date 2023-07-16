class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        #trick - removing 1 bit by doing n = n & (n-1)
        while n > 0:
            n = n & (n-1)
            count += 1
        return count
            