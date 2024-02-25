class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra's huh ? similar to bfs, but use a minheap
        
        #we need to create adjacency list
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v,w))
        
        
        visited = {}
        h = []
        heapify(h)
        
        #heap stores path length, node
        heappush(h, (0,k))
        
        while h:
            #print(h)
            curlen, curnode = heappop(h)
            visited[curnode] = curlen
            
            neighbors = adj[curnode] 
            for nei_node, nei_len in neighbors:
                if nei_node not in visited:
                    heappush(h, (curlen + nei_len ,nei_node))
            
            if len(visited) == n:
                return max(visited.values())
            
        #SSS Distance formed for all nodes. now we need max of those
        #print(visited)
        return -1
            
            
                    
            
                    
                
            
        