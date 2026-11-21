class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curMax = 0

        L, R = 0, len(heights) - 1

        while L < R:
            hL, hR = heights[L], heights[R]
            area = min(hL, hR) * (R - L)
            curMax = max(curMax, area)

            if hL <= hR:
                L += 1
            else:
                R -= 1
        
        return curMax
        