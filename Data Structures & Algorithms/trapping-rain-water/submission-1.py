class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        rightMax = []

        l, r = 0, len(height) - 1
        localLMax = 0
        localRMax = 0

        while l < len(height) and r >= 0:
            leftMax.append(localLMax)
            localLMax = max(localLMax, height[l])

            rightMax.append(localRMax)
            localRMax = max(localRMax, height[r])

            r -= 1
            l += 1
        
        rightMax.reverse()

        total = 0

        for i, bar in enumerate(height):
            lMax = leftMax[i]
            rMax = rightMax[i]

            if bar < lMax and bar < rMax:
                total += min(lMax, rMax) - bar
        
        return total

        