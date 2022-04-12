class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = []
        for ch in s:
            if ord(ch) in range(ord('A'),ord('Z')+1):
                ans.append(chr(ord(ch)+32))
            else:
                ans.append(ch)
        
        return ''.join(ans)