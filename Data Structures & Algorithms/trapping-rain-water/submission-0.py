class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) ==1 or len(height) == 2:
            return 0
        ## water stored at point i will be the min(maxLeft, maxRight) - h[i]
        ## set a pointer at the left and right endpoints, these will never store wayer
        ## track a max per pointer
        ## iterate the pointer with the smaller max

        ptr1, ptr2 = 0, len(height) - 1
        maxLeft, maxRight = height[ptr1], height[ptr2]
        storedWater = 0

        

        while ptr1 < ptr2:
            if maxLeft <= maxRight:
                ptr1 += 1
                water = maxLeft - height[ptr1]
                if water > 0:
                    storedWater += water
                maxLeft = max(maxLeft, height[ptr1])

            else:
                ptr2 -= 1
                water = maxRight - height[ptr2]
                if water > 0:
                    storedWater += water
                maxRight = max(maxRight, height[ptr2])
    
        return storedWater



        