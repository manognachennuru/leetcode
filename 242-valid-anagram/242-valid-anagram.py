class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #multiple ways to solve this
        #1. using a dic, list to store frequencies
        #2. using sort, sorted
        return sorted(s) == sorted(t)