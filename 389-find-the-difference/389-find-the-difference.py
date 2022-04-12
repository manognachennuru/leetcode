class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #form a dic with s
        #break it with t
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch,0) + 1
            
        for ch in t:
            if dic.get(ch): #not none,not zero
                dic[ch] = dic.get(ch,0) - 1
                
            else:
                return ch
            
            