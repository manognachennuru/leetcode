class Solution:
    def checkPalindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def longestPalindrome(self, s: str) -> str:
        #brute force
        if len(s) < 2:
            return s
        longest = s[0]
        for i in range(0,len(s)-1):
            for j in range(i,len(s)):
                if s[i] == s[j] and j-i+1 > len(longest):
                    current = self.checkPalindrome(s, i,j)
                    if current == True:
                        longest = s[i:j+1]
        return longest