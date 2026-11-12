class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            encoded += str(len(string)) + '#' + string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decodedList, i = [], 0

        while i < len(s):
            k = i
            while s[k] != '#':
                k += 1
            decodedList.append(s[k + 1: k + 1 + int(s[i:k])])
            i = k + 1 + int(s[i:k])
        
        return decodedList


