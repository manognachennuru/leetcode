class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        if n == 1:
            return 
        for i in range(0,n//2):
            for j in range(i,n-i-1):
                #copy top
                temp = mat[i][j]
            
                #left --> top
                mat[i][j] = mat[n-j-1][i]
                
                #bottom --> left
                mat[n-j-1][i] = mat[n-i-1][n-j-1]
                
                #right --> bottom
                mat[n-i-1][n-j-1] = mat[j][n-i-1]
            
                #right --> copied top
                mat[j][n-i-1] = temp
                
