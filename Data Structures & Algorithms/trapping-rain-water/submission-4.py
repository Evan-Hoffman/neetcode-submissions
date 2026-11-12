class Solution:
    def trap(self, height: List[int]) -> int:
        lMax, rMax = height[0], height[-1]
        l, r = 0, len(height) - 1

        water = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1

                trapped = min(lMax, rMax) - height[l]
                if trapped > 0:
                    water += trapped
                lMax = max(lMax, height[l])
            
            else:
                r -= 1
                trapped = min(lMax, rMax) - height[r]
                if trapped > 0:
                    water += trapped
                rMax = max(rMax, height[r])
        
        return water


        