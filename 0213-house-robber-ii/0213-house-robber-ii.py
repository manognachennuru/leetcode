class Solution:
    def helper(self, nums: List[int]) -> int:
        #print("nums in helper", nums)
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
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        else:
            takeone = self.helper(nums[0:len(nums)-1])
            discardone = self.helper(nums[1:])
            #print(takeone, discardone)
            return max(takeone, discardone)