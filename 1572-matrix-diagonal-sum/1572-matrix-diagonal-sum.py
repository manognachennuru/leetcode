class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)
        for i in range(0,n):
            res += mat[i][i] + mat[i][n-i-1]
            if i == n-i-1:
                res -= mat[i][n-i-1]
        return res