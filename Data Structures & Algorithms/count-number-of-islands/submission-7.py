class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]


        def mark_visited(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or grid[r][c] == '0'):
                return
            

            visited.add((r, c))

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                mark_visited(nr, nc)
            
            return
    
        total = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    mark_visited(r, c)
                    total += 1
        
        return total


        