class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(arr):
            #base case
            if len(arr) == 1:
                return [arr.copy()]
            
            perm = []
            temp = arr.copy()
            
            for num in temp:
                arr.remove(num)
                #print("num = ",num, "arr after removing = ", arr)
                rem = helper(arr) #gives permutations for remaining elements
                
                #print("rem = ",rem)
                #print("uff, [num] = [", num,"], rem = ", rem)
                
                for r in rem:
                    perm.append([num] + r)
                #print("perm", perm)
                
                arr.append(num)
                
            return perm
        
        return helper(nums)
        
                
        
        
        
        