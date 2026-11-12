class Solution:
    def isValid(self, s: str) -> bool:
        mapDict = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for character in s:
            if character not in mapDict:
                stack.append(character)
            else:
                if not stack or stack.pop() != mapDict[character]:
                    return False
        
        return True if not stack else False
































        # stack = []
        # closeMap = {")": "(", "]": "[", "}": "{"}
        # openSet = set(["(", "[", "{"])

        # for char in s:
        #     if char in openSet:
        #         stack.append(char)
        #     else:
        #         if len(stack):
        #             top = stack.pop()
        #             if top != closeMap[char]:
        #                 return False
        #         else:
        #             return False
        
        # return len(stack) == 0

        