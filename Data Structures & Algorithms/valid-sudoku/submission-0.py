class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## 
        cols = {}
        rows = {}
        squares = {}

        for i in range(9):
            cols[i] = set()
            rows[i] = set()
        
        for j in range(3):
            for k in range(3):
                squares[(j, k)] = set()
        
        for l in range(9):
            for h in range(9):
                element = board[l][h]
                if element != '.':
                    if element in cols[l]:
                        return False
                    if element in rows[h]:
                        return False
                    xCord = l // 3
                    yCord = h // 3

                    if element in squares[(xCord, yCord)]:
                        return False
                    
                    cols[l].add(element)
                    rows[h].add(element)
                    squares[(xCord, yCord)].add(element)
        
        return True