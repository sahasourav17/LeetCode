class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Intuition: matrix[r][c] = matrix[r][c] + min(top_left, top_above, top_right)
        r = len(matrix)
        c = len(matrix[0])

        for i in range(1, r):
            for j in range(c):
                if j == 0:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j+1])
                elif j == c-1:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j-1])
                else:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j-1], matrix[i-1][j+1])
        return min(matrix[-1])
