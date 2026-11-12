class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        curMax = -1
        stack = []

        for i, height in enumerate(heights):
            # curMax = max(curMax, height)
            idx = i
            while stack and height < stack[-1][0]:
                topH, topI = stack.pop()
                curMax = max(curMax, topH * (i - topI))
                idx = topI
            stack.append((height, idx))

        while stack:
            topH, topI = stack.pop()
            curMax = max(curMax, topH * (len(heights) - topI))
            # if not stack:
            #     stack.append((height, i))
            
            # elif height > stack[-1][0]:
            #     stack.append((height, i))
            
               
            
            # elif height == stack[-1][0]:
            #     curMax = max(curMax, height * (i - stack[-1][-1] + 1))
            
            # else:
            #     curMax = max(curMax, stack[-1][0] * (i - stack[-1][-1] + 1))
            #     stack.append((height, i))
        
        return curMax

        