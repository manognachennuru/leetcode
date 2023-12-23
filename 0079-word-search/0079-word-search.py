class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = set()
        
        def dfs(i, j, k):
            if k == len(word):
                return True
            
            if (i >= len(board) or j >= len(board[0])) or (i < 0 or j < 0) or ((i,j) in path) or (board[i][j] != word[k]):
                return False
            
            path.add((i,j))
            k += 1
            #check 4 sides
            res = dfs(i + 1, j, k) or dfs(i - 1, j, k) or dfs(i, j + 1, k) or dfs(i, j - 1, k)
                    
            path.remove((i,j))
            return res
        
        for i in range(len(board)):
            for j in range(0,len(board[0])):
                if dfs(i,j,0):
                    return True