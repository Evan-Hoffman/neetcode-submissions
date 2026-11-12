class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sSet, tSet = {}, {}

        for i in range(len(s)):
            sSet[s[i]] = sSet.get(s[i], 0) + 1
            tSet[t[i]] = tSet.get(t[i], 0) + 1
        
        return sSet == tSet





























        # if len(s) != len(t):
        #     return False

        # sCounter = Counter(s)
        
        # for char in t:
        #     if char not in sCounter:
        #         return False
            
        #     else:
        #         ct = sCounter.get(char)
        #         ct -= 1
        #         if ct == 0:
        #             sCounter.pop(char)
        #         else:
        #             sCounter[char] = ct
        
        # return True

        


        