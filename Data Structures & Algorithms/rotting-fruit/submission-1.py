class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        self.freshFruitsLeft = 0
        visited = set()

        ##Iterate through and add all rotten fruits to q, count up fresh fruits

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.freshFruitsLeft += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))

        def addSquare(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 0):
                return
            
            visited.add((r, c))
            grid[r][c] = 2
            q.append((r, c))            
            self.freshFruitsLeft -= 1

        
        mins = 0

        while q and self.freshFruitsLeft:
            for _ in range(len(q)):
                row, col = q.popleft()

                addSquare(row + 1, col)
                addSquare(row - 1, col)
                addSquare(row, col - 1)
                addSquare(row, col + 1)

            mins += 1
        
        return mins if not self.freshFruitsLeft else -1
        





                
        