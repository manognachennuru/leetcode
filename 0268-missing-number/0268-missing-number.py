class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #only use O(1) space
        res = 0
        for num in nums:
            res = res | (1 << num)
            
        #res has all 1 bits and one 0 bit
        #retreive the num corresponding to the 0 bit
        count = 0
        while res > 0:
            if res & 1:
                res = res >> 1
                count += 1
            else:
                return count
        return count
            