class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = [0] * 26
        for char in s1:
            target[ord(char) - ord('a')] += 1
        
        targetTuple = tuple(target)
        
        window = [0] * 26

        l = 0

        for r, char in enumerate(s2):
            window[ord(char) - ord('a')] += 1
            if r >= len(s1) - 1:
                if targetTuple == tuple(window):
                    return True
                else:
                    window[ord(s2[l]) - ord('a')] -= 1
                    l += 1
        
        return False


