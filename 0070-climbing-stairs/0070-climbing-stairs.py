class Solution:
    def helper(self, n, dp):
        if dp[n] != 0:
            return dp[n]
        else:
            for i in range(3,n+1):
                dp[i] = self.helper(i-1, dp) + self.helper(i-2, dp)
            return dp[n]
    
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        self.helper(n, dp)
        return dp[n]
        