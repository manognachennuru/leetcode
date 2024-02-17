class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        seen = set()
        n = len(grid)
        
        q.append((0,0,1)) #row, column, length
        seen.add((0,0)) #row and column
        
        while q:
            
            r, c, length = q.popleft()
            #print(r, c, length)
            
            if r < 0 or c < 0 or r >= n or c >= n: #invalid cell
                continue
                
            if grid[r][c] == 1: #unclear cell
                continue
            
            if r == (n-1) and c == (n-1): #reached bottom-right cell
                return length
                
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1), 
                         (r+1, c+1), (r+1, c-1), (r-1, c-1), (r-1, c+1)]    
            for nei in neighbors:
                if nei in seen: #neighbor already seen
                    continue
                nr, nc = nei
                
                seen.add((nr,nc)) #add into seen
                q.append((nr, nc, length + 1)) #add into q
                
        return -1
            
            
