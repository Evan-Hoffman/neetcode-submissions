class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        tempStack = []
        results = []

        def backtrack(openN, closedN):

            if closedN == openN == n:
                results.append("".join(tempStack))
                return
            
            if openN < n:
                tempStack.append("(")
                backtrack(openN + 1, closedN)
                tempStack.pop()
            
            if closedN < openN:
                tempStack.append(")")
                backtrack(openN, closedN + 1)
                tempStack.pop()
        
        backtrack(0, 0)
        return results
