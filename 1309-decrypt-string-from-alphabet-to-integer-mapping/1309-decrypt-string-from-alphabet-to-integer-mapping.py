class Solution:
    def freqAlphabets(self, s: str) -> str:
        from collections import deque
        q = deque()
        
        #trverse backwards
        i = len(s)-1
        while i >= 0:
            
            if s[i] == "#":
                n = s[i-2]+s[i-1]
                q.appendleft(chr(96+int(n)))
                i -= 3
            else:
                q.appendleft(chr(96+int(s[i])))
                i -= 1
        return ''.join(q)