class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ##[(40, 5), (28, 6)]
        ##[1, 4, 1, 2, 1, 0, 0]

        results = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while len(stack) and stack[-1][0] < temp:
                topTemp, topIndex = stack.pop()
                results[topIndex] = index - topIndex
            
            stack.append((temp, index))
        
        return results

        