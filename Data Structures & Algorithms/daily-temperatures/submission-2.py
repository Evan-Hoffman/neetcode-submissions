class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ##[(40, 5), (28, 6)]
        ##[1, 4, 1, 2, 1, 0, 0]

        #keep a stack of (temp, index)
        #iterate through the temps, while the top of the stack is lower temp:
        #    pop it
        #    add index dif to results array
        #add element to top of stack

        results = [0] * len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
            
            else:
                while stack and stack[-1][0] < temp:
                    lastTemp, lastI = stack.pop()
                    results[lastI] = i - lastI
                
                stack.append((temp, i))
        
        return results




































        # results = [0] * len(temperatures)
        # stack = []

        # for index, temp in enumerate(temperatures):
        #     while len(stack) and stack[-1][0] < temp:
        #         topTemp, topIndex = stack.pop()
        #         results[topIndex] = index - topIndex
            
        #     stack.append((temp, index))
        
        # return results

        