# @algorithm @lc id=898 lang=python3 
# @title transpose-matrix


from cn.Python3.mod.preImport import *
# @test([[1,2,3],[4,5,6],[7,8,9]])=[[1,4,7],[2,5,8],[3,6,9]]
# @test([[1,2,3],[4,5,6]])=[[1,4],[2,5],[3,6]]
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        new_matrix = [[None for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                new_matrix[j][i] = matrix[i][j]
            
        return new_matrix