class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, visited, lastHeight):
            if (min(row, col) < 0 or row == ROWS or col == COLS or (row, col) in visited or heights[row][col] < lastHeight):
                return
            
            visited.add((row, col))

            dfs(row - 1, col, visited, heights[row][col])
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            return

        for c in range(COLS):
            dfs(0, c, pac, -1)
            dfs(ROWS - 1, c, atl, -1)
        
        for r in range(ROWS):
            dfs(r, 0, pac, -1)
            dfs(r, COLS - 1, atl, -1)
        
        res = []

        for r, c in pac:
            if (r, c) in atl:
                res.append([r, c])
        
        return res
        