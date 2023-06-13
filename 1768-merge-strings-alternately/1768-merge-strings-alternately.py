class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        l1 = len(w1)
        l2 = len(w2)
        i,j = 0,0
        output = []
        while i < l1 and j < l2:
            output.append(w1[i])
            output.append(w2[j])
            i += 1    
            j += 1
        
        output.append(w1[i:])
        output.append(w2[j:])
        
        return ''.join(output)