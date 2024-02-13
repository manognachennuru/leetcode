class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #dfs - recursive
        #input is similar to adjacency list, no need to change
        def dfs(stack, paths, path):
            while stack:
                node = stack.pop()
                path.append(node)

                if node == (n-1):
                    #found path
                    paths.append(path.copy())
                    continue

                neighbors = graph[node]
                for neighbor in neighbors:
                    stack.append(neighbor)
                    dfs(stack, paths, path)
                    path.pop()

                #print(stack, paths, path)
            return 
        
        stack = []
        paths = []
        path = []
        n = len(graph)
        stack.append(0)
        dfs(stack, paths, path)
        return paths
        
        
            
                
                
        
        