class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        ptr = 0

        while ptr < len(s):
            ##get len:
            size = ""
            while s[ptr] != "#":
                size += s[ptr]
                ptr += 1
            
            res.append(s[ptr + 1: ptr + int(size) + 1])
        
            ptr += int(size) + 1
        
        return res
