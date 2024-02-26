class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #topological sorting, (Kahn's algorithm = using BFS) 
        
        adj = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
        
        queue = deque([k for k in range(numCourses) if indegree[k] == 0])
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            # Reduce in-degree for all the neighbors
            for neighbor in adj[node]:
                indegree[neighbor] -= 1

                # Add neighbor to Q if in-degree becomes 0
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == numCourses else []
                
        