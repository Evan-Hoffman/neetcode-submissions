import collections
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_cells = set()
        atlantic_cells = set()

        pq = collections.deque()
        aq = collections.deque()

        # pq = []
        # aq = []

        ##load pacific cells into q
        visited = set()

        for r in range(ROWS):
            pq.append([r, 0])
            pacific_cells.add((r, 0))
            aq.append([r, COLS - 1])
            atlantic_cells.add((r, COLS - 1))
        
        for c in range(COLS):
            pq.append([0, c])
            pacific_cells.add((0, c))
            aq.append([ROWS - 1, c])
            atlantic_cells.add((ROWS - 1, c))
        
        def check_cell(row, col, last_val, ocean_set, ocean_q):
            if row < 0 or row == ROWS or col < 0 or col == COLS or (row, col) in visited or heights[row][col] < last_val:
                return
            
            visited.add((row, col))
            ocean_set.add((row, col))
            ocean_q.append([row, col])


        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while pq:
            row, col = pq.popleft()

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                check_cell(nr, nc, heights[row][col], pacific_cells, pq)
        
        visited = set()

        while aq:
            row, col = aq.popleft()

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                check_cell(nr, nc, heights[row][col], atlantic_cells, aq)
        
        res = []

        for row, col in pacific_cells:
            if (row, col) in atlantic_cells:
                res.append([row, col])
        
        return res

        


        