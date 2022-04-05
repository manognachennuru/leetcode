class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        res = 0
        nums.sort(reverse = True)
        #print(nums)
        for i in range(0,len(nums)-2):
            if nums[i+1]+nums[i+2] > nums[i]:
                #print("nums [i,j,k] = ", nums[i],nums[j],nums[k])
                return nums[i]+nums[i+1]+nums[i+2]
                    
        return res
            