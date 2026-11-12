class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ## keep track of min length, min substring
        ## create a counter map
        ## increasing right ptr, add to counter map until you  achieve substring
        ## move left ptr, ejecting from counter as you go. if you lose valid substring,
        ## begin moving right again

        tCounter = {}

        for char in t:
            tCounter[char] = tCounter.get(char, 0) + 1

        minL = len(s)
        minString = ""

        counter = {}

        def checkContains() -> bool:
            for key, count in tCounter.items():
                if key not in counter or counter[key] < count:
                    return False
            
            return True
        
        
        l = 0
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1

            if checkContains():
                isValid = True

                while isValid and l < len(s):
                    if (minL > r - l):
                        minL = r - l
                        minString = s[l : r + 1]
                    
                    counter[s[l]] -= 1
                    if s[l] in tCounter and counter[s[l]] < tCounter[s[l]]:
                        isValid = False
                    
                    l += 1
        
        return minString

        # tCounter = {}

        # for char in t:
        #     tCounter[char] = tCounter.get(char, 0) + 1

        # minL = len(s)
        # minString = ""

        # counter = {}

        # def checkContains() -> bool:
        #     for key, count in tCounter.items():
        #         if key not in counter or counter[key] < count:
        #             return False
            
        #     return True
        

        # l = 0
        # for r in range(len(s)):
        #     counter[s[r]] = counter.get(s[r], 0) + 1
            
        #     while checkContains() and l < len(s):
        #         if (minL > r - l):
        #             minL = r - l
        #             minString = s[l : r + 1]
                
        #         counter[s[l]] -= 1
        #         if counter[s[l]] == 0:
        #             counter.pop(s[l])
                
        #         l += 1
        
        # return minString
                
                

