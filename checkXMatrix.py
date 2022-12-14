class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        '''
        Idea :
        While checking diagonals, To make easy to check other
        elements, I set the diagonal values to zero.

        '''
        for i in range(len(grid)):
            if grid[i][i] == 0 or grid[-i-1][i] == 0:
                return False
            else:
                grid[i][i] = 0
                grid[-i-1][i] = 0

        for row in grid:
            for elem in row:
                if elem != 0:
                    return False
        return True
