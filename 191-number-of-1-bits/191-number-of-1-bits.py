class Solution:
    def hammingWeight(self, n: int) -> int:
        # solution 1 from youtube
        # %2 will give us the last digit each time
        # bit shift is CPU efficient instead of dividing everytime
        count = 0
        while n != 0:
            count += n % 2
            n = n >> 1
        return count