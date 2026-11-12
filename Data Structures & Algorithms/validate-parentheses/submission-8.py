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

        