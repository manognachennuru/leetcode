class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #if adjacent element is same as next expected element
        #either go left, right, up, down (only 3 directions)
        #where do i start ? 
        
        k = 0
        path = set()
        
        def helper(k, i, j):
            if k == len(word):
                return True
            
            #print(i,j,"board[i][j] = ",board[i][j],"k = ",k, "word[k] = ", word[k])
            
            #if path used
            if tuple([i,j]) in path:
                return False
            
            #if out of board
            if i < 0 or j < 0:
                return False
            
            if i >= len(board) or j >= len(board[0]):
                return False
            
            if board[i][j] != word[k]:
                return False
                
            if board[i][j] == word[k]:
                k += 1
                path.add(tuple([i,j]))
                
            #call adjacent cells
            res = helper(k, i, j + 1) or helper(k, i, j-1) or helper(k, i+1, j) or helper(k, i-1, j)
            #print("returning res",res)
        
            path.remove(tuple([i,j]))
            return res
            
        #need to call helper on all cells
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if helper(0,i,j):
                    return True
        
        