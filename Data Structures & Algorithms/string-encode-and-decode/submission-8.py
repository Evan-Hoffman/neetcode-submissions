class Solution:
    ## ["Hello","World"]

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""

        for word in strs:
            encodedStr += str(len(word)) + "%" + word
        
        return encodedStr # '5%Hello5%World'

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            num = ""
            while s[i] != "%":
                num += s[i]
                i += 1
            
            res.append(s[i + 1: i + int(num) + 1])
            i = i + int(num) + 1
        
        return res


