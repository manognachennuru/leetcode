class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index , i = 0,1
        for i in range(0,len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return index+1
    
            