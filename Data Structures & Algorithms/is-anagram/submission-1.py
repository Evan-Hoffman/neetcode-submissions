class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounts = {}

        for character in s:
            if character in sCounts:
                sCounts[character] += 1
            else:
                sCounts[character] = 1
        
        for character in t:
            if character in sCounts:
                if sCounts[character] == 1:
                    sCounts.pop(character)
                else:
                    sCounts[character] -= 1
            else:
                return False

        return not any(sCounts)