
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #ok, let's do dfs
        #no need to monitor visited as the graph is directed
        #it is tough to do iteratively. You need to keep track of path at each step
        
        n = len(graph)
        stack = []
        stack.append((0, [0]))
        
        allPaths = []
        path = []
        
        while stack:
            node,path = stack.pop()
            
            if node == n-1:
                #found a path
                allPaths.append(path[:])
            
            for neighbor in graph[node]:
                stack.append((neighbor, path + [neighbor]))
                
        return allPaths