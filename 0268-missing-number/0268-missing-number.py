class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #XOR in one loop
        ans = len(nums)
        for i, num in enumerate(nums):
            ans ^= i
            ans ^= num
        return ans
            