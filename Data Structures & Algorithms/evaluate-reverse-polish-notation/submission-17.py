class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = set(['+', '-', '*', '/'])

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()

                if token == '+':
                    stack.append(first + second)
                elif token == '-':
                    stack.append(first - second)
                elif token == '*':
                    stack.append(first * second)
                elif token == '/':

                    stack.append(int(first / second))

        return stack[-1]











































        # stack = []
        
        # for token in tokens:

            # if token == "+" or token == "-" or token == "/" or token == "*":
            #     second = stack.pop()
            #     first = stack.pop()

            #     if token == "+":
            #         stack.append(int(first) + int(second))
            #     elif token == "-":
            #         stack.append(int(first) - int(second))
            #     elif token == "*":
            #         stack.append(int(first) * int(second))
            #     elif token == "/":
            #         stack.append(int(int(first) / int(second)))

            # else:
            #     stack.append(token)

                
        
        # return int(stack.pop())

        