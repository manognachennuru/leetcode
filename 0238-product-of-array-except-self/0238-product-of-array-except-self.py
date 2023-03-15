class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        output = [1]*len(nums)
        for i in range(0,len(nums)):
            output[i] = left
            left = left * nums[i]
            
        for i in range(len(nums)-1,-1,-1):
            output[i] *= right
            right = right * nums[i]
            
        return output