class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)

        for i in range(n):
            sum += mat[i][i]

        i = 0
        j = n-1

        while i < n and j >= 0:
            #  removing duplicate diagonal elements
            if i != j:
                sum += mat[i][j]
            i += 1
            j -= 1

        return sum