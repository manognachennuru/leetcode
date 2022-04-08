class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search o(log n) - solution - 
        #trying recursive approach
        def helper(low,high):
            while low <= high:
                mid = low + (high - low)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    return helper(low,mid - 1)
                else:
                    return helper(mid+1,high)
            return -1
    
        low = 0
        high = len(nums) - 1
        return helper(low,high)
        