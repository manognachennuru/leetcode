class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        perms = []
        
        def helper(nums):
            #base case
            if len(nums) == 1:
                return [nums.copy()]
            
            temp = nums.copy()
            perm = []
            
            for num in set(nums):
                
                temp.remove(num)
                #call helper on remaining values
                rem = helper(temp)
                
                #print("num = ", num, "temp = ", temp, "rem = ", rem)
                
                for r in rem:
                    perm.append(r + [num])
                
                temp.append(num)
            return perm
        
        return helper(nums)
                
                
        
        