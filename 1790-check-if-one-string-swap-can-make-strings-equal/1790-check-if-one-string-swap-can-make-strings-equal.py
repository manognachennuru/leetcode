class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        #they shld be diff only at 2 indexes
        indexes = []
        for i in range(0,len(s1)):
            if s1[i] != s2[i]:
                indexes.append(i)
            if len(indexes) > 2:
                return False
        if len(indexes) == 0:
            return True
        if len(indexes) == 1:
            return False
        
        #2 different, checking if they can be swapped to make strings equal
        if s1[indexes[0]] == s2[indexes[1]] and s1[indexes[1]] == s2[indexes[0]]:
            return True
        return False
        
                
            
                