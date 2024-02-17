class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #using bfs, 
        #iterative, use a queue, add current path to the queue
        #source is 0, destination is n-1
        #seen = set()
        n = len(graph)
        q = deque()
        q.append([0])
        
        paths = []
        path = []
        
        while q:
            path = q.pop()
            lastv = path[-1] 
            if lastv == (n-1):
                paths.append(path.copy())
                continue
            
            for nei in graph[lastv]:
                q.append(path + [nei])
                
        return paths
                
        
        
        
        
        