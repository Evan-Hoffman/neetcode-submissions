class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set()

        left, curMax = 0, 0

        for right in range(len(s)):
            if s[right] in uniques:
                curMax = max(curMax, len(uniques))

                while s[right] != s[left]:
                    uniques.remove(s[left])
                    left += 1
                uniques.remove(s[left])
                left += 1
            
            uniques.add(s[right])
        
        return max(curMax, len(uniques))





        