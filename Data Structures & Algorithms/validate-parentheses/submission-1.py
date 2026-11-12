class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openSet = {'[', '(', '{'}
        closeSet = {']', ')', '}'}
        
        for char in s:
            if char in openSet:
                stack.append(char)
            
            elif char in closeSet:
                if (len(stack) == 0):
                    return False
                
                topChar = stack.pop()

                if char == '}':
                    if topChar != '{':
                        return False
                elif char == ']':
                    if topChar != '[':
                        return False
                elif char == ')':
                    if topChar != '(':
                        return False
        if len(stack) == 0:
            return True
        
        return False
