class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #only 26 unique characters, create an array of frequencies for the strings and group the string based on that
        
        dic = {} #dictionary with keys as frequency arrays
        
        for string in strs:
            freqlist = [0]*26
            for char in string:
                index = ord(char) - 97
                freqlist[index] += 1
                
            if dic.get(str(freqlist)):
                dic[str(freqlist)].append(string)
            else:
                dic[str(freqlist)] = [string]
                
        return dic.values()
        
            
            
            
            