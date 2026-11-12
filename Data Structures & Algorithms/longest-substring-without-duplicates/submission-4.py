class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set()

        left, curMax = 0, 0

        for right in range(len(s)):
            while s[right] in uniques:
                uniques.remove(s[left])
                left += 1
            
            uniques.add(s[right])
            curMax = max(curMax, len(uniques))
        
        return curMax





        