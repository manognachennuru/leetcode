class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        dict = {}
        for char in s:
            dict[char] = dict.get(char,0) + 1
        for char in t:
            if dict.get(char):
                dict[char] = dict[char] - 1
            else:
                return False
        return True