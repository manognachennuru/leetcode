class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
            i += 1
            
        return index
        