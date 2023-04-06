class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            """
            Case 1: Not Closed Island
                    only when we went out of bound
            Case 2: Closed Island
            """
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS):
                return 0 # False
            if grid[r][c] == 1 or (r,c) in visited:
                return 1 # True

            visited.add((r,c))
            return min(dfs(r+1,c),
                    dfs(r-1,c),
                    dfs(r,c+1),
                    dfs(r,c-1))
        
        countClosedIsland = 0
        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c] and (r,c) not in visited:
                    countClosedIsland += dfs(r,c)
        return countClosedIsland
                    