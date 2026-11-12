class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCounts = {}

        for character in s:
            sCounts[character] = 1 + sCounts.get(character, 0)
        
        for character in t:
            if character in sCounts:
                if sCounts[character] == 1:
                    sCounts.pop(character)
                else:
                    sCounts[character] -= 1
            else:
                return False

        return not any(sCounts)