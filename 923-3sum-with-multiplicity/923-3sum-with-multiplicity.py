class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        #from solutions
        import collections
        count = collections.Counter(arr)
        keys = sorted(count)
        
        ans = 0
        mod = pow(10,9) + 7
        for i in range(0,len(keys)):
            T = target - keys[i]
            j = i
            k = len(keys) - 1
            while j <= k:
                if keys[j] + keys[k] < T:
                    j += 1
                elif keys[j] + keys[k] > T:
                    k -= 1
                #found a triplet.
                else:
                    
                    if i < j < k:
                        ans += count[keys[i]] * count[keys[j]] * count[keys[k]]
                    elif i == j < k:
                        ans += count[keys[i]] * (count[keys[i]] - 1)//2 * count[keys[k]]
                    elif i < j == k:
                        ans += count[keys[i]] * count[keys[j]] * (count[keys[j]] - 1)//2
                    else: #i == j == k
                        ans += count[keys[i]] * (count[keys[j]] - 1) * (count[keys[k]] - 2)//6
                    
                    
                    j += 1
                    k -= 1
        return ans % mod
                
                    
        