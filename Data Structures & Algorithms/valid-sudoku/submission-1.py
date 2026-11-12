class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]

        squares = {}

        for i in range(3):
            for j in range(3):
                squares[(i, j)] = set()
        

        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element != ".":

                    if element in rows[r] or element in cols[c] or element in squares[(r // 3, c // 3)]:
                        return False
                    
                    rows[r].add(element)
                    cols[c].add(element)
                    squares[(r // 3, c // 3)].add(element)
        
        return True





























        # rows = [set() for i in range(9)]
        # cols = [set() for i in range(9)]
        # squares = defaultdict(set)

        # # for i in range(3):
        # #     for j in range(3):
        # #         squares[(i, j)] = set()
        
        # for r in range(9):
        #     for c in range(9):
        #         val = board[r][c]
        #         if val.isdigit():
        #             if val in rows[r] or val in cols[c] or val in squares[(r // 3, c // 3)]:
        #                 return False
        #             else:
        #                 rows[r].add(val)
        #                 cols[c].add(val)
        #                 squares[(r // 3, c // 3)].add(val)
        
        # return True

        