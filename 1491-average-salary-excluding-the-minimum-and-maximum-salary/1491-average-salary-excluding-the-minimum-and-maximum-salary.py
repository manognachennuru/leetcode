class Solution:
    def average(self, salary: List[int]) -> float:
        minval,maxval,s,l = 1_000_000,0,0,0
        
        for val in salary:
            l += 1
            s += val
            
            if val < minval:
                minval = val
            if val > maxval:
                maxval = val
    
        return (s - minval - maxval) / (l - 2)