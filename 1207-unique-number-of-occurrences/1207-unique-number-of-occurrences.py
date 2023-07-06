class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        #formed a dictionary of keys, frequencies
        for key in arr:
            if dic.get(key) == None:
                dic[key] = 1
            else:
                dic[key] += 1
        
        freqs = dic.values()
        
        #check if freqs are unique
        return len(freqs) == len(set(freqs))