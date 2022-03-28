class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        0 - 00
        1 - 01
        2 - 10
        3 - 11
        
        4 - 100
        5 - 101
        6 - 110
        7 - 111
        
        8 - 1000
        9 - 1001 
        10 - 1010
        11 - 1011
        12 - 1100
        13 - 1101
        14 - 1110
        15 - 1111
        
        16 - 10000
        '''
        
        #using dynamic proggramming, memoization
        #using the previous solutions, we are trying to calculate current sol
        # base - case 
        dp = []
        power = 1
        
        for index in range(0,n+1):
            #basecase
            if power == 1:
                dp = [0,1,1,2]
                
            if index == 2**power:
                power += 1
                l = len(dp)
                for j in range(0,l):
                    dp.append(1+dp[j])

        return dp[0:n+1]

        