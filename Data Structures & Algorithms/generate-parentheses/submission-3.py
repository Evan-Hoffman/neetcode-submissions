class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []
        

        def backtrack(openCt, closedCt):
            if closedCt == openCt == n:
                res.append(''.join(stack))
                return
            
            if openCt < n:
                stack.append('(')
                backtrack(openCt + 1, closedCt)
                stack.pop()

            if closedCt < openCt:
                stack.append(')')
                backtrack(openCt, closedCt + 1)
                stack.pop()
            
            return
        
        backtrack(0, 0)
        return res

        