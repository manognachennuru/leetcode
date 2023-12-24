class Solution(object):
    def subsets(self, nums):
        res = [[]]
        
        def helper(n):
            size = len(res)
            for i in range(0, size):
                #print("res[i] = ", res[i], "type(res[i]) = ", type(res[i]))
                subset = res[i][:]
                subset.append(n)
                res.append(subset)
                
        for num in nums:
            helper(num)
            
        return res
        
        
        