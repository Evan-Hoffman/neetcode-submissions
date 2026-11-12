class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        includedSet = set()

        def markIsland(r, c) -> bool:
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in includedSet or grid[r][c] == '0'):
                return False
            
            includedSet.add((r, c))

            markIsland(r - 1, c)
            markIsland(r + 1, c)
            markIsland(r, c - 1)
            markIsland(r, c + 1)

            return True
        
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in includedSet:
                    markIsland(r, c)
                    count += 1
        
        return count





        