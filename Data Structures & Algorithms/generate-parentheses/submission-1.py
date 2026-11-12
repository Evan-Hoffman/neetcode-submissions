class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def helper(openCt, closeCt):
            if openCt == closeCt == n:
                result.append("".join(stack))
                return
            
            if openCt < n:
                stack.append('(')
                helper(openCt + 1, closeCt)
                stack.pop()
            
            if closeCt < openCt:
                stack.append(')')
                helper(openCt, closeCt + 1)
                stack.pop()

        
        helper(0, 0)

        return result


        