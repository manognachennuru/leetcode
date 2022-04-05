class Solution:
    def checkPalindrome(self, s, l,r):
        while l<r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            #found a mismatched pair - try both deletions
            if s[left] != s[right]:
                return self.checkPalindrome(s,left+1,right) or self.checkPalindrome(s,left,right-1)
            left += 1
            right -= 1
        return True
    
                