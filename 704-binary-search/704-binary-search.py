class Solution:
    def helper(self,nums,target,low,high):
        if low > high:
            return -1
        mid = low + (high - low)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.helper(nums,target,low,mid - 1)
        else:
            return self.helper(nums,target,mid+1,high)
    
    def search(self, nums: List[int], target: int) -> int: 
        return self.helper(nums,target,0,len(nums)-1)
        
    