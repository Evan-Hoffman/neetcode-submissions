class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = []

        def helper(openCt, closedCt, n):
            if openCt == n and closedCt == n:
                output.append(''.join(stack))
                stack.pop()
                return

            if openCt < n:
                stack.append('(')
                helper(openCt + 1, closedCt, n)
                
            
            if closedCt < openCt and closedCt < n:
                stack.append(')')
                helper(openCt, closedCt + 1, n)
            
            if stack:
                stack.pop()
                        
            return
        
        helper(0, 0, n)
        return output
            

































        # result = []
        # stack = []

        # def helper(openCt, closeCt):
        #     if openCt == closeCt == n:
        #         result.append("".join(stack))
        #         return
            
        #     if openCt < n:
        #         stack.append('(')
        #         helper(openCt + 1, closeCt)
        #         stack.pop()
            
        #     if closeCt < openCt:
        #         stack.append(')')
        #         helper(openCt, closeCt + 1)
        #         stack.pop()

        
        # helper(0, 0)

        # return result


        