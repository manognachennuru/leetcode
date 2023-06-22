class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        left = 0
        right = len(l)-1
        
        while left < right:
            #both vowels
            if l[left] in ['a','e','i','o','u','A','E','I','O','U'] and l[right] in ['a','e','i','o','u','A','E','I','O','U'] :
                l[left],l[right] = l[right],l[left]
                left += 1
                right -= 1
            #one vowel
            elif l[left] in ['a','e','i','o','u','A','E','I','O','U']:
                right -= 1
            elif l[right] in ['a','e','i','o','u','A','E','I','O','U']:
                left += 1
            else:
                left += 1
                right -= 1
        
        return ''.join(l)