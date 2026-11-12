class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        colSet, posDiagSet, negDiagSet = set(), set(), set()
        curBoard = []

        def dfs(r):
            if r == n:
                res.append(curBoard.copy())
                return
            
            row = ['.'] * n

            for c in range(n):
                if c not in colSet and r - c not in negDiagSet and n - 1 - c - r not in posDiagSet:
                    colSet.add(c)
                    negDiagSet.add(r - c)
                    posDiagSet.add(n - 1 - c - r)
                    row[c] = 'Q'
                    curBoard.append(''.join(row))
                    dfs(r + 1)
                    curBoard.pop()
                    row[c] = '.'
                    posDiagSet.remove(n - 1 - c - r)
                    negDiagSet.remove(r - c)
                    colSet.remove(c)
        
        dfs(0)
        return res
            
