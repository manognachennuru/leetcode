class Solution:
    def hammingWeight(self, n: int) -> int:
        #from discussions
        '''If we have number n, then n&(n-1) will remove the rightmost in binary representation of n. For example if n = 10110100, then n & (n-1) = 10110100 & 10110011 = 10110000, where & means bitwize operation and. Very convinient, is it not? What we need to do now, just repeat this operation until we have n = 0 and count number of steps.'''
        count = 0
        while n > 0:
            n = n & (n-1)
            count += 1
        return count