class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ## keep track of min length, min substring
        ## create a counter map
        ## increasing right ptr, add to counter map until you  achieve substring
        ## move left ptr, ejecting from counter as you go. if you lose valid substring,
        ## begin moving right again

        tCounter = {}
        counter = {}

        for char in t:
            tCounter[char] = tCounter.get(char, 0) + 1

            if char not in counter:
                counter[char] = 0

        minL = len(s)
        minString = ""

        have = 0
        need = len(tCounter)
        
        l = 0
        for r in range(len(s)):
            if s[r] in tCounter:
                counter[s[r]] = counter.get(s[r], 0) + 1

                if counter[s[r]] == tCounter[s[r]]:
                    have += 1
                
                while have == need and l < len(s):
                    if s[l] in tCounter:
                        
                        
                        counter[s[l]] -= 1
                        if counter[s[l]] < tCounter[s[l]]:
                            have -= 1
                            if (minL > r - l):
                                minL = r - l
                                minString = s[l : r + 1]
                        
                    l += 1
        
        return minString
                
                

