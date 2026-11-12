class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeMap = {")": "(", "]": "[", "}": "{"}
        openSet = set(["(", "[", "{"])

        for char in s:
            if char in openSet:
                stack.append(char)
            else:
                if len(stack):
                    top = stack.pop()
                    if top != closeMap[char]:
                        return False
                else:
                    return False
        
        return len(stack) == 0

        