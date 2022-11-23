class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1, dic2 = {}, {}
        for i in range(0,len(s)):
            dic1[s[i]] = dic1.get(s[i],0) + 1
            dic2[t[i]] = dic2.get(t[i],0) + 1
        for ch in dic1:
            if dic1[ch] != dic2.get(ch,0):
                return False
        return True
    