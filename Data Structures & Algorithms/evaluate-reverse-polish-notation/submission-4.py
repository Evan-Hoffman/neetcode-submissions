class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opSet = {"+", "-", "*", "/"}

        for token in tokens:
            if token in opSet and len(stack) >= 2:
                second = stack.pop()
                first = stack.pop()

                if token == "+":
                    stack.append(str(int(second) + int(first)))
                elif token == "-":
                    stack.append(str(int(first) - int(second)))
                elif token == "*":
                    stack.append(str(int(first) * int(second)))
                elif token == "/":
                    res = int(int(first) / int(second))
                    stack.append(str(res))
            else:
                stack.append(token)
        
        return int(stack.pop())

        