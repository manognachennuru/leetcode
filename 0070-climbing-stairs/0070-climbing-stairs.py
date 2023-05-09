class Solution:
    def helper(self, n, dp):
        if dp[n] == 0:
            dp[n] = self.helper(n-1, dp) + self.helper(n-2, dp)
        return dp[n]
        
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        return self.helper(n,dp)
        
    