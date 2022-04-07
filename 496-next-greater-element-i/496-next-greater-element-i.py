class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import deque
        stk = deque()
        dic = {}
        
        for key in nums2:
            while len(stk) and stk[-1] < key:
                dic[stk.pop()] = key
            stk.append(key)
            
        while len(stk):
            dic[stk.pop()] = -1
            
        result = []
        for num in nums1:
            result.append(dic[num])
            
        return result
            