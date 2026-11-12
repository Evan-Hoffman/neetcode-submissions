class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ##pointer at the start and the back
        ## set max area
        ## while ptr1 < ptr2
        ## compare to max
        ## drop the smallest and iterate

        ptr1, ptr2 = 0, len(heights) -1

        curMax = 0

        while ptr1 < ptr2:
            area = min(heights[ptr1], heights[ptr2]) * (ptr2 - ptr1)
            curMax = max(curMax, area)

            if heights[ptr2] >= heights[ptr1]:
                ptr1 += 1
            else:
                ptr2 -= 1
        
        return curMax

        