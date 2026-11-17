class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        curMax = 0

        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                last, last_i = stack.pop()
                curMax = max(curMax, (last * (i - last_i)))
                start = last_i

            stack.append((height, start))
        
        while stack:
            height, i = stack.pop()
            curMax = max(curMax, height * (len(heights) - i))
        
        return curMax
            

        