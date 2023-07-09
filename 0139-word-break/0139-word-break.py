class Solution:
    def helper(self, s, wordDict, notaword):
        if len(s) == 0: return True 
        if s in wordDict: return True
        if s in notaword: return False
        for i in range(1, len(s)):
            if self.helper(s[0:i], wordDict, notaword) == False:
                notaword.add(s[0:i])
                continue
            elif self.helper(s[i:], wordDict, notaword) == False:
                notaword.add(s[i:])
            else:
                #both are not false
                wordDict.add(s)
                return True
        return False
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        notaword = set()
        wordDict = set(wordDict)
        return self.helper(s, wordDict, notaword)
        

