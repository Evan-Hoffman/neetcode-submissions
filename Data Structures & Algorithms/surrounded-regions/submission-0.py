class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        safeOs = set()

        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in safeOs or board[r][c] == 'X'):
                return
            
            safeOs.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            return
        
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O' and (row, col) not in safeOs:
                    board[row][col] = 'X'
        