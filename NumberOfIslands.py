class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        islandCount = 0

        def dfs(r,c):

            if(r < 0 or r >= m or
               c < 0 or c >= n or
               grid[r][c] == '0'): return

            grid[r][c] = '0' # marking as visited
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islandCount += 1
                    dfs(i,j)
        return islandCount