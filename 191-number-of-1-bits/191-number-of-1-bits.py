class Solution:
    def hammingWeight(self, n: int) -> int:
        #print(n) n is integer
        #n is int, we need to count '1' bits in binary representation
        #count while you convert into binary representation
        
        count = 0
        p = 32
        
        while n != 0:
            if pow(2,p) <= n:
                count += 1
                n -= pow(2,p)
            p -= 1
        return count