class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,num in enumerate(nums):
            if dic.get(target-num) is not None:
                return [i,dic.get(target-num)]
            else:
                dic[num] = i
        return []
                
        
        