class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #dfs - recursive
        #input is similar to adjacency list, no need to change
        #NO NEED OF STACK VARIABLE IN DFS RECURSIVE
        def dfs(node):
            path.append(node)

            if node == (n-1):
                #found path
                paths.append(path.copy())
                return

            neighbors = graph[node]
            for neighbor in neighbors:
                dfs(neighbor)
                path.pop()

                #print(stack, paths, path)
            return 
        
        paths = []
        path = []
        n = len(graph)
        dfs(0)
        return paths
        
        
            
                
                
        
        