class Solution:
    def isalnum(c):
        #my implementation of built-in function
        if ord('A') < ord(c) < ord('Z') or ord('a') < ord(c) < ord('z') or ord('0') < ord(c) < ord('9'):
            return True
        return False
        
        
    def isPalindrome(self, s: str) -> bool:
        #don't use all built in functions and extra memory
        #learn to use two pointers.
        
        l = 0 #left pointer
        r = len(s)-1 #right pointer 
        
        while l < r:
            
            while l<r and not s[l].isalnum():
                l += 1
                
            while r>l and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True
        
        