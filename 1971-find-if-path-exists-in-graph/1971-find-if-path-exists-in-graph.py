class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #dfs - recursive
        
        #create adjacency list
        adj_list = [[] for i in range(n)]
        for edge in edges:
            a, b = edge
            adj_list[a].append(b)
            adj_list[b].append(a)
            
        
        
        seen = set()
        
        def dfs(node):
            #print("entered dfs with node = ", node)
            if node == destination:
                return True
            
            seen.add(node)
            for nei in adj_list[node]:
                if nei not in seen:
                    seen.add(nei)
                    if dfs(nei):
                        return True
                else:
                    continue
                
            return False
        
        return dfs(source)
        