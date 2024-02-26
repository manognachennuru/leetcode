class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #now try top sort using BFS (Kahn's algorithm) (uses in degree concept)
    
        #create adj list
        adj = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        visited = set()
        q = deque()

        #in the queue, we need all nodes with indegree 0
        q.extend([k for k in range(0,len(indegree)) if indegree[k] == 0])

        while q:
            node = q.popleft()
            visited.add(node)
            for nei in adj[node]:
                #decrease in degree
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    #add to queue
                    q.append(nei)

        return len(visited) == numCourses