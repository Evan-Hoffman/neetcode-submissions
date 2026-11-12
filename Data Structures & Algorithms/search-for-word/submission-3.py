class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.visited = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in self.visited or board[r][c] != word[i]:
                return False
            
            self.visited.add((r, c))
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            self.visited.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and (r, c) not in self.visited:
                    if dfs(r, c, 0):
                        return True
        
        return False




        