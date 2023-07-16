class Solution:
    def reverseBits(self, n: int) -> int:
        #you've to generate reverse bit as you remove bits from n
        rev = 0

        #used for inorder to not-miss the trailing zeroes
        for _ in range(0,32):
            d = n % 2
            rev = rev*2 + d
            n = n >> 1
        
        return rev
            