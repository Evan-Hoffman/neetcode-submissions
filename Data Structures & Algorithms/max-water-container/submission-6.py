class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        curMax = 0

        while left < right:
            curMax = max(curMax, (right - left) * min(heights[left], heights[right]))

            if heights[right] > heights[left]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                if heights[left + 1] > heights[right - 1]:
                    left += 1
                else:
                    right -= 1
        
        return curMax






























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
        