class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ##BFS:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        curMax = 0
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def bfs(r, c) -> int:
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            size = 1
            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc

                    if (min(nr, nc) < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited or grid[nr][nc] == 0):
                        continue
                    
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    size += 1

            return size
                

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curMax = max(curMax, bfs(r, c))
        
        return curMax











        ##Recursive DFS:
        # ROWS, COLS = len(grid), len(grid[0])
        # visited = set()
        # curMax = 0

        # def dfs(r, c):
        #     if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 0):
        #         return 0
            
        #     visited.add((r, c))


        #     return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1 and (r, c) not in visited:
        #             curMax = max(curMax, dfs(r, c))
        
        # return curMax
        