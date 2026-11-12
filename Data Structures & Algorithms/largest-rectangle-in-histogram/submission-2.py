class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        curMax = -1
        stack = []

        for i, height in enumerate(heights):
            idx = i
            while stack and height < stack[-1][0]:
                topH, topI = stack.pop()
                curMax = max(curMax, topH * (i - topI))
                idx = topI
            stack.append((height, idx))

        while stack:
            topH, topI = stack.pop()
            curMax = max(curMax, topH * (len(heights) - topI))

        return curMax

        