class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #What if elements of nums2 are stored on disk, 
        #and the memory is limited such that 
        #you cannot load all elements into the memory at once?

        result = []
        #create a dict for nums1
        dict1 = defaultdict(int)
        for num1 in nums1:
            dict1[num1] += 1
        
        #now traverse through num2 and see if that element is in nums1
        #if it does, remove it from dict1, and add into result
        for num2 in nums2:
            if dict1[num2]: 
                result.append(num2)
                dict1[num2] -= 1
        
        return result