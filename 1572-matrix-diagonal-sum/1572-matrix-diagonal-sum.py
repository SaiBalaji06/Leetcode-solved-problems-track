class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sum_diagonal = 0

        for i in range(len(mat)):
            sum_diagonal += mat[i][i]
            if abs(i - (len(mat) - i - 1)) != 0:
                sum_diagonal += mat[i][len(mat) - i - 1]
        
        return sum_diagonal

        