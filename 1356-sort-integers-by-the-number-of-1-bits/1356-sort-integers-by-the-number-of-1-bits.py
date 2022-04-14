class Solution:
    #dumb attempt
    def countBits(self,num):
        return bin(num).count('1')
    
    def sortByBits(self, nums: List[int]) -> List[int]:
        dic = {}
        for num in nums:
            count = self.countBits(num)
            dic[count] = dic.get(count,[]) + [num]
            
        output = []
        sortedCounts = sorted(list(dic.keys()))
        for key in sortedCounts:
            numsForCount = sorted(dic[key])
            output += numsForCount
        return output
            
    