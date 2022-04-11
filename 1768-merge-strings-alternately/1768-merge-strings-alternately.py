class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1),len(word2))
        output = []
        for i in range(0,m):
            output += [word1[i], word2[i]]
        if len(word1) > len(word2):
            output += [word1[i+1:]]
        if len(word1) < len(word2):
            output += [word2[i+1:]]
            
        return ''.join(output)
            
            