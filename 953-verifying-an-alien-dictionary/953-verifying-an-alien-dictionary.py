class Solution:
    def checkOrder(self,dic,w1,w2):
        m = min(len(w1),len(w2))
        for i in range(m):
            if dic[w1[i]] < dic[w2[i]]:
                return True
            elif dic[w1[i]] > dic[w2[i]]:
                return False
        return False if len(w1) > len(w2) else True
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i,o in enumerate(order):
            dic[o] = i
        
        index = 1
        while index < len(words):
            if not self.checkOrder(dic,words[index-1],words[index]):
                return False
            index += 1
        return True
            
        
            