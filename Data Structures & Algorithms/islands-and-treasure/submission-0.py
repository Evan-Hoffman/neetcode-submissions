class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        MAX_INT = 2147483647

        def bfs(r, c):
            visited = set()
            visited.add((r, c))

            q = collections.deque([(r, c)])

            dist = 0

            while q:

                for i in range(len(q)):
                    row, col = q.popleft()

                    if grid[row][col] == 0:
                        grid[r][c] = dist
                        return
                    
                    for dr, dc in dirs:
                        nr, nc = dr + row, dc + col

                        if (min(nr, nc) < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited or grid[nr][nc] == -1):
                            continue
                        
                        q.append((nr, nc))
                        visited.add((nr, nc))
                
                dist += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == MAX_INT:
                    bfs(r, c)
        
        

        