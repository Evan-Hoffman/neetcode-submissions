class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## create a counter of s1's letters

        ##find first letter in s2 thats in the counter
        ## create a copy of counter
            ##while letter in dict or size != 0
            ##moving right from the first letter, decrement in counter each letter
        ##if loop ends cause hit a letter not in dict, reset copy dict

        counter = {}

        for letter in s1:
            counter[letter] = counter.get(letter, 0) + 1
        
        ptr1 = 0

        while ptr1 < len(s2):
            if s2[ptr1] not in counter:
                ptr1 += 1

            else:
                copyCounter = counter.copy()
                ptr2 = ptr1

                while ptr2 < len(s2) and s2[ptr2] in copyCounter:
                    ct = copyCounter[s2[ptr2]] - 1
                    if ct == 0:
                        copyCounter.pop(s2[ptr2])
                    else:
                        copyCounter[s2[ptr2]] -= 1
                    ptr2 += 1
                
                if not len(copyCounter):
                    return True
                
                ptr1 += 1
            
        return False



        