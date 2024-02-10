class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #let's try doing dfs
        #create an adjacency list first
        adj_lis = defaultdict(list)
        for edge in edges:
            a,b = edge
            adj_lis[a].append(b)
            adj_lis[b].append(a)
        
        stack = []
        stack.append(source)
        seen = set()
        
        while stack:
            node = stack.pop()
            
            if node == destination:
                return True
            
            if node in seen:
                continue
            seen.add(node)           

            for neighbor in adj_lis[node]:
                stack.append(neighbor)
                
        return False
            
            
            
                