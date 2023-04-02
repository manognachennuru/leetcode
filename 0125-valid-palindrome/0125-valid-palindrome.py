class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lst = []
        for char in s:
            if char.isalnum():
                lst.append(char)
        if lst[::-1] == lst:
            return True
        return False
        
        
        