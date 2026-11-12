class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')' : '(', ']': '[', '}': '{'}

        for chara in s:
            if chara not in closeToOpen:
                stack.append(chara)
            else:
                if not stack or closeToOpen[chara] != stack[-1]:
                    return False
                stack.pop()
        
        return True if not stack else False