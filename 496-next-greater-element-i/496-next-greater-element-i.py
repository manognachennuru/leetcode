class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #from youtube
        nums1Index = {val : index for index,val in enumerate(nums1)}
        stk = collections.deque()
        result = [-1]*len(nums1)
        
        for current in nums2:
            while len(stk) and stk[-1] < current:
                resIndex = nums1Index.get(stk.pop())
                result[resIndex] = current
                
            if nums1Index.get(current) != None:
                 stk.append(current)
                    
        return result