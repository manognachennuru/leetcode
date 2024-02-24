# UnionFind class
class unionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
    
class Edge:
    def __init__(self, point1, point2, weight):
        self.point1 = point1
        self.point2 = point2
        self.weight = weight
        
    def __lt__(self, other):
        return self.weight < other.weight
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # now, let's try using an edge class
        
        n = len(points)
        uf = unionFind(n)
        result = 0
        count = 0 # to count number of edges
        pq = []
        num = 0
        
        for i in range(0, n-1):
            for j in range(i+1, n):                    
                xi, yi = points[i]
                xj, yj = points[j]
                
                weight = abs(xi-xj) + abs(yi-yj)
                
                edge = Edge(i, j, weight)
                pq.append(edge)
                
        # Convert pq into a heap.
        heapq.heapify(pq)
         
        while pq and count != (n-1):
                edge = heapq.heappop(pq)
                
                #if it isn't forming a cycle
                if not uf.isConnected(edge.point1, edge.point2):
                    #add edge to disjoint set
                    uf.union(edge.point1, edge.point2)
                    
                    #add weight to result
                    result += edge.weight
                    count += 1
        
        return result
        
                
                
            
        
        