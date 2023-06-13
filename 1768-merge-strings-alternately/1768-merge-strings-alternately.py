class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        l1 = len(w1)
        l2 = len(w2)
        i,j = 0,0
        output = []
        while True:
            if i<l1:
                output.append(w1[i])
                i += 1
            if j<l2:
                output.append(w2[j])
                j += 1
            if i == l1 and j == l2:
                break
        return ''.join(output)