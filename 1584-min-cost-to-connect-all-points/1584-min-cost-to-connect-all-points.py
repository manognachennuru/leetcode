# UnionFind class
class unionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
                
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

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
        visited = [False]*n
        
        #add all edges from vertex 0
        x1, y1 = points[0]
        for j in range(1, n):
            #calculate distance to all vertices
            x2, y2 = points[j]
            weight = abs(x1-x2) + abs(y1-y2)

            edge = Edge(0, j, weight)
            pq.append(edge)
                
        # Convert pq into a heap.
        heapq.heapify(pq)
        
        visited[0] = True
        
        while pq and count != (n-1):
            edge = heapq.heappop(pq)
            point1 = edge.point1
            point2 = edge.point2
            weight = edge.weight
            if not visited[point2]:
                result += weight
                visited[point2] = True
                for j in range(n):
                    if not visited[j]:
                        distance = abs(points[point2][0] - points[j][0]) + \
                                   abs(points[point2][1] - points[j][1])
                        heapq.heappush(pq, Edge(point2, j, distance))
                count += 1
                
        return result
                
                
            
        
        