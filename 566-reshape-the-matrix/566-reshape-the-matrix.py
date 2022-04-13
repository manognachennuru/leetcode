class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        
        res = [[0 for _ in range(0,c)] for _ in range(0,r)]
        print(res)
        p,q = 0,0 #r,c
        for i in range(0,len(mat)):
            for j in range(0,len(mat[0])):
                res[p][q] = mat[i][j]
                
                if q == c-1:
                    p += 1
                    q = 0
                else:
                    q += 1
                
                
        return res
                    
                