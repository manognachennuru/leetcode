class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        dic = collections.Counter(arr)
        
        freqs = dic.values()
        
        #check if freqs are unique
        return len(freqs) == len(set(freqs))