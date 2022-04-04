class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                #finding the index where we need to change
                index = i - 1
                break
        else:
            return nums.sort()
        
        
        for i in range(len(nums)-1,-1,-1):
            #swapping val at index with it's next greater element from right side
            #at index, we'll have correct element
            #we'll be left with decresing order after index
            if nums[index] < nums[i]:
                #swap
                nums[i] , nums[index] = nums[index], nums[i]
                break
        
        
        left = index + 1
        right = len(nums) - 1
        while left < right:
            #reversing [index+1: ] elements 
            #so that they'll be in increasing order,instead of decreasing order
            nums[left] , nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
        
            
            
            
            
            
            