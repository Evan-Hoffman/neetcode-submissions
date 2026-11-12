class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create a curMax, and a set
        #using 2 pointers left and right:
            #if element in right not in set, add to set
            #if element in right in set, compare max and curmax, then 
                #while left is not element at right, pop from left

        uniques = set()

        left, curMax = 0, 0

        for right in range(len(s)):
            while s[right] in uniques:
                uniques.remove(s[left])
                left += 1
            
            uniques.add(s[right])
            curMax = max(curMax, len(uniques))
        
        return curMax





        