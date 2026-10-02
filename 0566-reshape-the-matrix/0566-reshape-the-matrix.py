class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if mat and r * c == len(mat) * len(mat[0]):

            temp = []

            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    temp.append(mat[i][j])
                
            res_mat = []
            a = 0
            for i in range(r):
                t = []
                for j in range(c):
                    t.append(temp[a])
                    a += 1
                res_mat.append(t)
            
            return res_mat
            
        return mat



