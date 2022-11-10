class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col = len(board),len(board[0])
        '''
            declaring a path for keeping track which
            position we've already visited.As we can't use same
            element twice.
        '''
        path = set()

        def dfs(r,c,i):

            # initial condition
            if i == len(word):
                return True
            '''
                Now, we need to check basically three 
                conditions:
                1. Boundary Condition
                2. If current char of the word != element of that board positon
                3. Already visited or not.
            '''
            if (r < 0 or c < 0 or
                r >= row or c >= col or
                word[i] != board[r][c] or
                (r,c) in path):

                return False

            path.add((r,c))

            # print(path)

            '''
                Considering 4 connected neighbors.
                As we can only move horizontaly and vertically.
                then run our dfs function for every 4 neighbors of current element.
            '''
            res = (dfs(r+1,c,i+1) or
                  dfs(r-1,c,i+1) or
                  dfs(r,c+1,i+1) or
                  dfs(r,c-1,i+1))

            path.remove((r,c))

            return res

        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False
    '''
        Time Complexity : O(n*m*4^len(word))
    '''
