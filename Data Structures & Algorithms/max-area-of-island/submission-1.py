class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        curMax = 0
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r, c))

            count = 0

            for dr, dc in dirs:
                count += dfs(r + dr, c + dc)
            
            return 1 + count
            
    


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    curMax = max(curMax, dfs(r, c))
        
        return curMax
        