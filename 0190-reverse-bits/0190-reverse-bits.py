class Solution:
    def reverseBits(self, n: int) -> int:
        #you've to generate reverse bit as you remove bits from n
        rev = 0

        #used for inorder to not-miss the trailing zeroes
        for _ in range(0,32):
            # n & 1 gives last bit
            rev = rev << 1 | (n & 1)
            n = n >> 1
        
        return rev
            