class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## k must be between 1 and the max pile in the list
        ##using binary search to narrow down, iterate through the piles with number k
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = (lo + hi) // 2

            if self.canIEatInK(piles, h, mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo
        
    def canIEatInK(self, piles: List[int], h: int, k: int) -> bool:
        hoursLeft = h
        for pile in piles:
            hoursLeft -= math.ceil(pile / k)
        
        return True if hoursLeft >= 0 else False
        
        