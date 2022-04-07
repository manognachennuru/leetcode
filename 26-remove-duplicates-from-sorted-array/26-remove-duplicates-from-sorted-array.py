class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index , i = 0,1
        for i in range(0,len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        
        #need to check last value
        if nums[index] != nums[-1]:
            index += 1
            nums[index] = nums[-1]
        
        return index + 1
    
            