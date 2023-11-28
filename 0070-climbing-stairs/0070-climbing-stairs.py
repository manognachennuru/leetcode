class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [1,2]:
            return n
        self.dp = [1]*(n+1)
        self.dp[1] = 1
        self.dp[2] = 2
        for i in range(2,n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[-1]
        