class Solution:
    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
        # declare running Min starting at float("inf")
        # take a counter of target string and get len(unique keys) as target matches
        # create an empty dict for len(t):
            #  add chars from s
            # check if is matching corresponding in target counter, if so, increment runningMatches


        minString = ""
        runningMin = float("inf")

        targets = Counter(t)
        targetMatches = len(targets)

        runningCounter = {}
        runningMatches = 0

        left = 0

        for right in range(len(s)):
            if runningMatches != targetMatches:
                toAdd = s[right]
                runningCounter[toAdd] = runningCounter.get(toAdd, 0) + 1
                if toAdd in targets:
                    if runningCounter[toAdd] == targets[toAdd]:
                        runningMatches += 1
            
            while runningMatches == targetMatches:
                if runningMin > right - left + 1:
                    minString = s[left: right + 1]
                    runningMin = right - left + 1
                
                toRem = s[left]
                runningCounter[toRem] -= 1
                if toRem in targets:
                    if runningCounter[toRem] + 1 == targets[toRem]:
                        runningMatches -= 1
                left += 1
        
        return minString
                



                




































        ##create a counter dict of the target t, a dict for s/window, a min length var
        ## a numMatches count, and targetMatches based on size of unique letters in t
        ##using sliding window go through s:
            ## while numMatches ct === targetMatches:
                ##compare length to minLength
                ##remove letter at left pointer from window dict and if that letter was in targetDict, decrement targetMatches
            ##if the numMatches ct !== targetMatches:
                ##add letter at right pointer

        # minString = ""
        # toMatch = Counter(t)
        # windowDict = {}
        # targetMatches = len(toMatch.keys())
        # numMatches = 0

        # l = 0

        # for r in range(len(s)):
        #     if numMatches != targetMatches:
        #         toInsert = s[r]
        #         windowDict[toInsert] = windowDict.get(toInsert, 0) + 1
        #         if toInsert in toMatch and toMatch[toInsert] == windowDict[toInsert]:
        #             numMatches += 1
            
        #     while numMatches == targetMatches:
        #         if minString == "" or len(minString) > r - l + 1:
        #             minString = s[l: r + 1]
        #         toRem = s[l]
        #         windowDict[toRem] -= 1
        #         if toRem in toMatch and toMatch[toRem] > windowDict[toRem]:
        #             numMatches -= 1
        #         l += 1
        
        # return minString





        