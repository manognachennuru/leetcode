class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sorting
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
            
        nums.sort()
        
        longest_streak = 0
        current_streak = 1
        
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i] == nums[i+1] - 1:
                current_streak += 1
            else:
                longest_streak = max(current_streak, longest_streak)
                current_streak = 1
        
        longest_streak = max(current_streak, longest_streak)    
        return longest_streak