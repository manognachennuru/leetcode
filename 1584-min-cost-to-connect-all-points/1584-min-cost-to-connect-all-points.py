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
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # heh, graph problem to find min spanning tree
        # can we use Kruskals algorithm ? 
        # calculate all distances first
        # make a dictionary with weight: point1, point2 : 
        # sort them based on weights
        # for each edge, if it doesn't make a cycle, add it's score
        # add edge into visted set
        # break when number of edges = n-1
        
        uf = unionFind(len(points))
        result = 0
        count = 0 # to count number of edges
        Wedge = defaultdict(list)
        num = 0
        
        for i in range(0, len(points)-1):
            for j in range(i+1, len(points)):                    
                xi, yi = points[i]
                xj, yj = points[j]
                
                weight = abs(xi-xj) + abs(yi-yj)
                Wedge[weight].append((points[i], points[j]))
         
        #print("Weights to edges = ", Wedge)
        #print("vertexes to nums = ", vertextoNum)
        #now we have a dict with weight: all edges with that weight
        for weight in sorted(Wedge.keys()):
            for edge in Wedge[weight]:
                pointA, pointB = edge
                
                #if it isn't forming a cycle
                if not uf.isConnected(points.index(pointA), points.index(pointB)):
                    #add edge to disjoint set
                    uf.union(points.index(pointA), points.index(pointB))
                    
                    #add weight to result
                    #print("adding edge = (",pointA, pointB,") and the weight is", weight)
                    result += weight
                    count += 1
                
                    if count == (len(points)-1):
                        #formed MST
                        return result
        
        return result
        
                
                
            
        
        