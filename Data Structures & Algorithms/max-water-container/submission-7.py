class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curMax = 0

        l, r = 0, len(heights) - 1

        while l < r:
            curMax = max(curMax, min(heights[l], heights[r]) * (r - l))

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return curMax
        