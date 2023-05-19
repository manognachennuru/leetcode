class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        dic = defaultdict(list)
        for i, a in enumerate(arr):
            dic[a].append(i)
            
        output = [0]*len(arr)
        
        for element in dic:
            indices = dic[element]
            l = len(indices)
            
            prefixSum = 0
            suffixSum = sum(indices)
            
            for c, i in enumerate(indices):
                prefixSum +=  i
                suffixSum -= i
                
                output[i] = ((c+1)*i - prefixSum) + (suffixSum - (l-c-1)*i )
                
        return output