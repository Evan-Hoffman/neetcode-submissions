class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        visited = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            visited.add((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc

                    if (min(nr, nc) < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited or grid[nr][nc] == '0'):
                        continue
                    
                    q.append((nr, nc))
                    visited.add((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    count += 1
        
        return count

