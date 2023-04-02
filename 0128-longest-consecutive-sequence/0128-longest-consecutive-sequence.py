class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #same as brute force, but optimized to get o(n)
        
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            #we are actually building sequence if that number is not already 
            #of a previously created larger sequence
            #in other words, check if the num is start of a sequence
            
            if num - 1 not in num_set:
            
                length = 0

                while num + length in num_set:
                    length += 1 
 
                longest = max(longest, length)
            
        return longest