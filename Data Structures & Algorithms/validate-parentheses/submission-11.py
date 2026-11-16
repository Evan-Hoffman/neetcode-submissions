class Solution:
    def isValid(self, s: str) -> bool:
        openChars = set(['(', '[', '{'])
        pairings = {')': '(', ']': '[', '}': '{'}

        stack = []

        for char in s:
            if char in openChars:
                stack.append(char)

            elif len(stack) and stack[-1] == pairings[char]:
                stack.pop()

            else:
                return False

        return len(stack) == 0             
              
        