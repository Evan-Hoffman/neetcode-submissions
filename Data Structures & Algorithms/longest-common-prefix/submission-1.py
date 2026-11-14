class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        ptr = 0

        while ptr < len(strs[0]):
            cur = strs[0][ptr]
            for string in strs:
                if ptr == len(string):
                    return strs[0][0: ptr]
                if string[ptr] != cur:
                    return strs[0][0: ptr]
                
            ptr += 1
        
        return strs[0][0: ptr]
            

        