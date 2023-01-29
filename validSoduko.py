class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checkRow = [set() for i in range(9)] # for checking digit repetition in row
        checkColumn = [set() for i in range(9)] # for checking digit repetition in column
        subGrid = [[set() for j in range(3)] for i in range(3)] # 3x3 grid
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if ((board[r][c] in checkRow[r]) or 
                    (board[r][c] in checkColumn[c]) or 
                    (board[r][c] in subGrid[r//3][c//3])):
                    return False
                checkRow[r].add(board[r][c])
                checkColumn[c].add(board[r][c])
                subGrid[r//3][c//3].add(board[r][c])
        return True
