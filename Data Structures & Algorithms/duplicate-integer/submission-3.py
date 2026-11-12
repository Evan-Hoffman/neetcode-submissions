class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            
            numSet.add(num)
        
        return False























        # numSet = set()

        # for num in nums:
        #     if num in numSet:
        #         return True
        #     else:
        #         numSet.add(num)
        
        # return False
         