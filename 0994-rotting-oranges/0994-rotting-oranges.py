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
        
        while True:
             
            statusChange = False
            #print("minutes = ", minutes)
            for r in range(0, rows):
                for c in range(0, cols):
                    if grid[r][c] == 2: #rotten orange
                        if (r, c) not in visited:
                            q.append((r,c)) 
                            visited.add((r,c))
                        

            while q:
                r, c = q.popleft() #always pop left for queue
                
                neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                #print("rotting orange is at ", r, c)
                for nr, nc in neighbors: 
                    #check if indices are valid
                    #print("nieghbors are ", nr, nc)
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        statusChange = True
            
            if statusChange == False:
                break
            
            minutes += 1 
                
        #now check if you have a fresh orange or not
        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == 1: #fresh orange
                    return -1
        return minutes
        
            
                    
              
        
        