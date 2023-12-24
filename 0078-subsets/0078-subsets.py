class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #backtracking - just form UNIQUE subsets
        result = []
        
        subset = []
        def dfs(i):
            #base case
            if i >= len(nums):
                result.append(subset.copy())
                return
                
            #for all elements, we have 2 options. either to add it or ignore it.
            #choose that element
            subset.append(nums[i])
            dfs(i+1)
            
            #dont choose that element
            subset.pop()
            dfs(i+1)
            
            
        dfs(0)
        return result
                    
                
                