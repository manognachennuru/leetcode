class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0]*(len(s)+1)
        if s[0] == '0':
            return 0
        
        dp[0] = 1    
        dp[1] = 1
        
        for k in range(2, len(s)+1):
            count = 0
            #verify if decode is possible
            if s[k-1] == '0' and s[k-2] not in ['1','2']:
                return 0
            #adding single digit combinations
            if s[k-1] != '0':
                count += dp[k-1]
            #adding double digit combinations
            if s[k-2] != '0':
                if int(s[k-2]+s[k-1]) < 27:
                    count += dp[k-2]
            dp[k] = count
        return dp[len(s)]