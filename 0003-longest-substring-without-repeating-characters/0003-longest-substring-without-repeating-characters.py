class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        left, right, longest = 0,0,0
        for right in range(0,len(s)):
            c = s[right]
            if c not in dic:
                dic[c] = right
                
            else:
                #update dictionary value for char c
                #update left to previous index of repeated character
                
                longest = max(longest, right - left)
                
                #remove elements from previous left to repeated element
                
                newleft = dic[c]+1
                for index in range(left,dic[c]+1):
                    del dic[s[left]]
                    left += 1
                
                left = newleft
                dic[c] = right
                
            right += 1
        #calculate length of last substring
        longest = max(longest, right - left)
        
        return longest
        