class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    # column
                    for p in range(m):
                        if matrix[p][j] != 0:
                            matrix[p][j] = '#'
                    # row
                    for q in range(n):
                        if matrix[i][q] != 0:
                            matrix[i][q] = '#'
        # print(matrix)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0
