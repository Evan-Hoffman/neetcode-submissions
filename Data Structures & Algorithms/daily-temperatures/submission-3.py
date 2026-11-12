class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ##create a stack
        ##iterate thru temps, for each temp:
        ## while temp is warmer than top of stack, pop top, edit res array with diff
        ## add to stack with index

        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                topT, topI = stack.pop()
                res[topI] = i - topI
            stack.append((temp, i))
        
        return res



        