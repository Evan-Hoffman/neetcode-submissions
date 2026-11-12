class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ##we need to find the k between 1 and max(piles)
        lo, hi = 1, max(piles)

        while lo < hi:
            k = (lo + hi) // 2

            if self.canIEatInH(piles, k, h):
                hi = k
            else:
                lo = k + 1
        
        return lo
    

    def canIEatInH(self, piles: List[int], k: int, h: int) -> bool:
        hoursLeft = h

        for pile in piles:
            hoursLeft -= math.ceil(pile / k)
        
        return True if hoursLeft >= 0 else False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        ## k must be between 1 and the max pile in the list
        ##using binary search to narrow down, iterate through the piles with number k
    #     lo, hi = 1, max(piles)

    #     while lo < hi:
    #         mid = (lo + hi) // 2

    #         if self.canIEatInK(piles, h, mid):
    #             hi = mid
    #         else:
    #             lo = mid + 1
        
    #     return lo
        
    # def canIEatInK(self, piles: List[int], h: int, k: int) -> bool:
    #     hoursLeft = h
    #     for pile in piles:
    #         hoursLeft -= math.ceil(pile / k)
        
    #     if hoursLeft < 0:
    #         return False
        
    #     return True
           
            



   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    #     low, high = 1, max(piles)

    #     while low < high:
    #         k = (low + high) // 2
    #         if self.canEatInK(piles, k, h):
    #             high = k
    #         else:
    #             low = k + 1
        
    #     return low
    
    # def canEatInK(self, piles, k, h): 
    #         hourLeft = h
            
    #         for pile in piles:
    #             hourLeft -= math.ceil(pile / k)

    #             if hourLeft < 0:
    #                 return False
            
    #         return True
    

        
        