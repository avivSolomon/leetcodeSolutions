class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        n, m = len(mat), len(mat[0])
        if r*c != n*m:
            return mat
        num = []
        for row in mat:
            num += row
        return [num[c*i:c*(i+1)] for i in range(r)]
