class UnionFind:
    def __init__(self,size):
        n = size
        self.root = [0]*n
        for i in range(len(self.root)):
            self.root[i] = i
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        self.root[rootX] = rootY
        return
        
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
    
    
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        
        return uf.isConnected(source, destination)