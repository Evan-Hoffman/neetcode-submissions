class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        lmax, rmax = height[left], height[right]
        total = 0

        while left < right:
            if lmax <= rmax:
                left += 1
                water = lmax - height[left]
                total += water if water > 0 else 0
                lmax = max(lmax, height[left])
            else:
                right -= 1
                water = rmax - height[right]
                total += water if water > 0 else 0
                rmax = max(rmax, height[right])
        
        return total































        # total = 0

        # left, right = 0, len(height) - 1

        # lMax, rMax = height[left], height[right]

        # while left < right - 1:
        #     if lMax <= rMax:
        #         left += 1
        #         water = min(rMax, lMax) - height[left]
        #         total += water if water > 0 else 0
        #         lMax = max(lMax, height[left])
            
        #     else:
        #         right -= 1
        #         water = min(rMax, lMax) - height[right]
        #         total += water if water > 0 else 0
        #         rMax = max(rMax, height[right])
        
        # return total




        