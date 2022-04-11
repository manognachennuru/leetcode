class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        #from discussions
        return ''.join(a + b for a, b in zip_longest(w1, w2, fillvalue=''))
            