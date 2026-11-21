class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        LMax, RMax = height[L], height[R]
        volume = 0


        while L < R:
            if LMax <= RMax:
                volume += LMax - height[L]
                L += 1
                LMax = max(LMax, height[L])
            else:
                volume += RMax - height[R]
                R -= 1
                RMax = max(RMax, height[R])
        
        return volume


        