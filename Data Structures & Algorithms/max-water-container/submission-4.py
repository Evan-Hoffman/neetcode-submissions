class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curMax = 0

        left, right = 0, len(heights) - 1

        while left < right:
            newArea = min(heights[left], heights[right]) * (right - left)
            curMax = max(newArea, curMax)

            if heights[left] <=  heights[right]:
                left += 1
            else:
                right -= 1
        
        return curMax
        