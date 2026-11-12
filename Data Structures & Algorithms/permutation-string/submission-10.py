class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## create two arrays of len 26
        ##initiate one array with the ords of s1, this is target arr
        ##using a sliding window of size len(s1), iterate over s2
            ##modify the second array, dropping/add chars as you go, comparing to target
                
        if len(s1) > len(s2):
            return False

        target, rolling = [0] * 26, [0] * 26
        
        left, right = 0, 0

        while right < len(s2):
            ##building initial window
            if right - left < len(s1):
                target[(ord(s1[right]) - ord('a'))] += 1
                rolling[(ord(s2[right]) - ord('a'))] += 1
                right += 1
            
            else:
                if target == rolling:
                    return True
                
                rolling[(ord(s2[left]) - ord('a'))] -= 1
                rolling[(ord(s2[right]) - ord('a'))] += 1
                left += 1
                right += 1
        
        return target == rolling













        # target = [0] * 26
        # for char in s1:
        #     target[ord(char) - ord('a')] += 1
        
        # targetTuple = tuple(target)
        
        # window = [0] * 26

        # l = 0

        # for r, char in enumerate(s2):
        #     window[ord(char) - ord('a')] += 1
        #     if r >= len(s1) - 1:
        #         if targetTuple == tuple(window):
        #             return True
        #         else:
        #             window[ord(s2[l]) - ord('a')] -= 1
        #             l += 1
        
        # return False


