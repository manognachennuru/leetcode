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
        foundDiff = False
        while left < right:
            if s[left] != s[right]:
                if foundDiff:
                    return False
                foundDiff = True
                if s[left] == s[right - 1] and s[left + 1] == s[right]:
                    return self.checkPalindrome(s,left+1,right) or self.checkPalindrome(s,left,right-1)
                
                if s[left] == s[right - 1]:
                    right -= 1
                elif s[left + 1] == s[right]:
                    left += 1
                
                else:
                    #2 chars shld be deleted
                    return False
            else:
                left += 1
                right -= 1
        return True
    
                