class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            #only one house
            return nums[0]
        if n == 2:
            #two houses
            return max(nums[0],nums[1])
        dp = [0]*(n+1)
        dp[1] = nums[0]
        dp[2] = max(nums[0],nums[1])
        for i in range(3,len(nums)+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return dp[n]