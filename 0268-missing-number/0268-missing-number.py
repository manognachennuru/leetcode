class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #XOR
        s = set(range(0, len(nums)+1))
        ans = 0
        for num in s:
            ans ^= num 
        for num in nums:
            ans ^= num
        return ans
            