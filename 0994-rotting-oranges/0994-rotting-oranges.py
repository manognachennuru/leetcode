class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #for each minute, do dfs for all cells with value 2.
        #return minutes if no cell has value 1
        #return -1 if the grid doesn't change in a minute. 
        
        #how do i use bfs
        
        if len(grid) == 0:
            return -1
        
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        visited = set()
        fresh = 0
        
        #print("minutes = ", minutes)
        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2: #rotten orange
                    if (r, c) not in visited:
                        q.append((r,c)) 
                        visited.add((r,c))

        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft() #always pop left for queue

                neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                #print("rotting orange is at ", r, c)
                for nr, nc in neighbors: 
                    #check if indices are valid
                    #print("neighbors are ", nr, nc)
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            
            minutes += 1 
        
        return minutes if not fresh else -1
        
            
                    
              
        
        