class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]* (n+1)
        target = 2
        for i in range(1,n+1):
            #odd = even + 1
            if (i % 2) != 0:
                dp[i] = dp[i-1] + 1
                continue
            if i == target:
                target *= 2
                dp[i] = 1
            else:
                dp[i] = 1 + dp[i-target//2]
        return dp