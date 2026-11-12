class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ##BFS:
        ROWS, COLS = len(board), len(board[0])
        q = collections.deque()

        def addCell(r, c):
            if (min(r, c) >= 0 and r < ROWS and c < COLS and board[r][c] == 'O'):
                board[r][c] = 'T'
                q.append((r, c))
        
        
        for row in range(ROWS):
            addCell(row, 0)
            addCell(row, COLS - 1)
        
        for col in range(COLS):
            addCell(0, col)
            addCell(ROWS - 1, col)
        
        while q:
            r, c = q.popleft()

            addCell(r - 1, c)
            addCell(r + 1, c)
            addCell(r, c - 1)
            addCell(r, c + 1)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'
        ##DFS:
        # ROWS, COLS = len(board), len(board[0])

        # def dfs(r, c):
        #     if (min(r, c) < 0 or r == ROWS or c == COLS or board[r][c] != 'O'):
        #         return
            
        #     board[r][c] = 'T'
        #     dfs(r - 1, c)
        #     dfs(r + 1, c)
        #     dfs(r, c - 1)
        #     dfs(r, c + 1)
        #     return
        
        # for row in range(ROWS):
        #     dfs(row, 0)
        #     dfs(row, COLS - 1)
        
        # for col in range(COLS):
        #     dfs(0, col)
        #     dfs(ROWS - 1, col)
        
        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if board[row][col] == 'O':
        #             board[row][col] = 'X'
        #         elif board[row][col] == 'T':
        #             board[row][col] = 'O'
        