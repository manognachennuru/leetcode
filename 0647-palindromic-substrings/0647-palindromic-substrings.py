class Solution:
    def checkPalindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def countSubstrings(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        count = len(s) #to include one letter sub-strings
        print(count)
        for i in range(0,len(s)-1):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    current = self.checkPalindrome(s, i,j)
                    if current == True:
                        count += 1
        return count