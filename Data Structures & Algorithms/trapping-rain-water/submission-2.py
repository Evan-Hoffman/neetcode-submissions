class Solution:
    def trap(self, height: List[int]) -> int:

        total = 0

        left, right = 0, len(height) - 1

        lMax, rMax = height[left], height[right]

        while left < right - 1:
            if lMax <= rMax:
                left += 1
                water = min(rMax, lMax) - height[left]
                total += water if water > 0 else 0
                lMax = max(lMax, height[left])
            
            else:
                right -= 1
                water = min(rMax, lMax) - height[right]
                total += water if water > 0 else 0
                rMax = max(rMax, height[right])
        
        return total




        