class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        #initialise last one
        dp[len(nums)-1] = 1
        for i in range(len(nums)-1,-1,-1):
            for j in range(i,len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            #print("i = ", i, "nums[i] = ", nums[i], "dp[i] = ", dp[i])
        return max(dp)