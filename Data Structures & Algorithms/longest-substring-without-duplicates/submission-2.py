class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## two pointers
        ## second pointer moves to next char
            ## if not in set, add to set, increment ptr
            ## if is in set
                ##check len(set) to curMax, set if larger
                ##move first ptr over until you hit the repeated char, popping from set as you go

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        maxLen = 1
        uniques = set()
        uniques.add(s[0])

        ptr1, ptr2 = 0, 1

        while ptr2 < len(s):
            charPtr2 = s[ptr2]
            if charPtr2 in uniques:
                

                while s[ptr1] != charPtr2:
                    uniques.remove(s[ptr1])
                    ptr1 += 1
                
                ptr1 += 1
                ptr2 += 1

            else:
                uniques.add(charPtr2)
                ptr2 += 1
                maxLen = max(maxLen, len(uniques))
        
        return maxLen




        