class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = float('-inf')
        prefix = 1
        suffix = 1
        for i in range(0, len(nums)):
            prefix *= nums[i]
            suffix *= nums[len(nums)-i-1]
            maxprod = max(maxprod, prefix, suffix)
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
        return maxprod
    
        