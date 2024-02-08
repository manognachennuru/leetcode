class UnionFind:
    def __init__(self, size):
        n = size
        self.root = [0]*size
        for i in range(0, size):
            self.root[i] = i
        self.count = n
            
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootX] = rootY
            self.count -= 1
        
        return
        
    def isConnected(self, x, y):
        return self.find[x] == self.find[y]
    
    def getCount(self):
        return self.count
    
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        uf = UnionFind(size)
        
        rows = len(isConnected)
        cols = len(isConnected[0])
        
        for r in range(rows):
            for c in range(cols):
                if isConnected[r][c] == 1:
                    uf.union(r, c)
                    
        return uf.getCount()
                    
                    
                    