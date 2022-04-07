class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index , i = 0,1
        while i < len(nums):
            if nums[i] == nums[index]:
                i += 1
                continue
            
            index += 1
            nums[index] = nums[i]
            i += 1
        
        #need to check last value
        if nums[index] != nums[-1]:
            index += 1
            nums[index] = nums[-1]
        
        return index + 1
    
            