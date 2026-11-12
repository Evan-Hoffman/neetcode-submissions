class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for string in strs:
            n = len(string)
            encodedString += str(n) + '#' + string
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        i = 0
        results = []

        while i < len(s) - 1:

            length = ""

            while s[i].isdigit():
                length += s[i]
                i += 1
            
            lenInt = int(length)

            results.append(s[i + 1: i + lenInt + 1])

            i = i + lenInt + 1
    
        return results


