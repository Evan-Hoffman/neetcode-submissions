class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ##BFS:
        ROWS, COLS = len(grid), len(grid[0])
        includedSet = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            includedSet.add((r, c))

            while q:
                row, col = q.popleft()
                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if (nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == '1' and (nr, nc) not in includedSet):
                        q.append((nr, nc))
                        includedSet.add((nr, nc))

        ct = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c] == '1' and (r, c) not in includedSet):
                    bfs(r, c)
                    ct += 1
        
        return ct




        ##Recursive DFS:
        # ROWS, COLS = len(grid), len(grid[0])
        # includedSet = set()

        # def markIsland(r, c):
        #     if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in includedSet or grid[r][c] == '0'):
        #         return
            
        #     includedSet.add((r, c))

        #     markIsland(r - 1, c)
        #     markIsland(r + 1, c)
        #     markIsland(r, c - 1)
        #     markIsland(r, c + 1)
        
        # count = 0
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == '1' and (r, c) not in includedSet:
        #             markIsland(r, c)
        #             count += 1
        
        # return count





        