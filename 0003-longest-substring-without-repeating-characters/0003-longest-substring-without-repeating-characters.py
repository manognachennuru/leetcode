class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left, right, longest = 0,0,0
        while right < len(s):
            c = s[right]
            if c not in charSet:
                charSet.add(c)
                
            else:
                while c in charSet:
                    charSet.remove(s[left])
                    left += 1
                    
                charSet.add(c)
                
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest
        