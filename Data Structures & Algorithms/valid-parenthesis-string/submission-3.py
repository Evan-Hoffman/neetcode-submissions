class Solution:
    def checkValidString(self, s: str) -> bool:

        leftStack = []
        asterStack = []

        for i, c in enumerate(s):
            if c == '(':
                leftStack.append(i)
            elif c == '*':
                asterStack.append(i)
            elif c == ')':
                if leftStack:
                    leftStack.pop()
                elif asterStack:
                    asterStack.pop()
                else:
                    return False
        
        if len(leftStack) > len(asterStack):
            return False
        
        while len(leftStack):
            paren, aster = leftStack.pop(), asterStack.pop()
            if paren > aster:
                return False
                
        return True

        