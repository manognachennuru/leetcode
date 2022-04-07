class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] == val:
                right += 1
            
            else:
                if right == len(nums):
                    return left
                #print("left = ",left,"right = ",right)
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
        return left
                
            
        
        