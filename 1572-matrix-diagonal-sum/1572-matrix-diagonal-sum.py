class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)
        for i in range(0,n):
            res += mat[i][i] + mat[i][n-i-1]
        return res - mat[n//2][n//2] if n%2 != 0 else res