class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sum_diagonal = 0

        for i in range(len(mat)):
            sum_diagonal += mat[i][i]
            if len(mat) % 2 != 0:
                if i != len(mat) // 2:
                    sum_diagonal += mat[i][len(mat) - i - 1]
                    print(mat[i][i], mat[i][len(mat) - i - 1])
            else:
                sum_diagonal += mat[i][len(mat) - i - 1]
        
        return sum_diagonal

        