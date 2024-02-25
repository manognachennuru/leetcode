class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #you might have a cyclic or acyclic graph. 
        # with a cyclic graph, we can't finish all the courses
        
        adj = [[] for _ in range(0,numCourses)]        #bi --> ai
        indegree = [0 for _ in range(0, numCourses)]
        
        #first create adjacency list
        for a, b in prerequisites:
            if a == b:
                return False
            adj[b].append(a)
            indegree[a] += 1
            
        visited = set()
        finished = set()
        node = None
        
        
        
        def dfs(node):
            #base case? 
            # print("node = ", node)
            
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    if dfs(nei) == True:
                        return True
                        
                if nei in visited and nei not in finished:
                    #found a cycle
                    return True
                
            finished.add(node)
        
        
        zero_indegree = []
        #from where should you start dfs ? 
        # a point where in degree is 0
        for i in range(0, len(indegree)):
            if indegree[i] == 0:
                zero_indegree.append(i)
        
        # print("indegree = ", indegree)
        # print("zero_indegree nodes are", zero_indegree)
        
        if len(zero_indegree) == 0:  #found no node with 0 indegree
            return False
        
        for node in zero_indegree:
            #now call dfs
            if dfs(node): #found a cycle --> can't finish courses
                return False
        
        return True if len(finished) == numCourses else False
        
            
            