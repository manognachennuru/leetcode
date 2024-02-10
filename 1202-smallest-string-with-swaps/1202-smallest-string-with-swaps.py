class UnionFind:
    def __init__(self, size):
        n = size
        self.root = [0]*size
        for i in range(0, size):
            self.root[i] = i
            
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
        
    def isConnected(self, x, y):
        return self.find[x] == self.find[y]
    
    def getRoot(self):
        return self.root
    
    
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        result = list(s)
        n = len(s)
        uf = UnionFind(n)
        
        for pair in pairs:
            uf.union(pair[0], pair[1])
            
        root = uf.getRoot()
        
        rootToComponent = defaultdict(list)
        for i in range(0, len(root)):
            key = uf.find(root[i])
            rootToComponent[key] += [i]
            
        for key in rootToComponent:
            indices = rootToComponent[key]
            characters = []
            for i in indices:
                characters += [s[i]]
                
            characters.sort()
            j = 0
            for i in indices:
                result[i] = characters[j]
                j += 1
                
        return ''.join(result)
        
        