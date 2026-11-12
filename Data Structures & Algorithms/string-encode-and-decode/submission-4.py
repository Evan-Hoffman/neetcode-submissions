class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for string in strs:
            n = len(string)
            encoded = encoded + str(n) + '#' + string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        ptr1 = 0
        ptr2 = 1
        results = []

        while ptr2 < len(s):
            if s[ptr2] != '#':
                ptr2 += 1
            else:
                length = int(s[ptr1: ptr2])
                results.append(s[ptr2 + 1: ptr2 + length + 1 ])
                ptr1 = ptr2 + length + 1
                ptr2 = ptr1 + 1
        
        return results


