class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        #bruteforce, backtracking -- will get TLE 
        #introduced zero_count to enable early stopping (see official solution)
        
        res = 10**10
        dist = [0 for _ in range(0,k)] #distribution of cookies among the children
        zero_count = k
        n = len(cookies)
        
        def choose(i, zero_count):
            nonlocal res
            if (n-i) < zero_count:
                return 10**10
            
            
            if i == len(cookies):
                #return max(dist)
                #done with choosing all cookies to the distribution
                res = min(res, max(dist))
                return res
            
            for j in range(0,k):
                if dist[j] == 0:
                    zero_count -= 1
                
                dist[j] += cookies[i]
                choose(i+1, zero_count)
                dist[j] -= cookies[i]
                
                if dist[j] == 0:
                    zero_count += 1
                    
            return res
        
        res = choose(0, zero_count)
        return res
                