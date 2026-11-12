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
        



















    

# def encode(self, strs: List[str]) -> str:
#         encodedString = ""

#         for string in strs:
#             encodedString += str(len(string)) + "#" + string
        
#         return encodedString


# def decode(self, s: str) -> List[str]:
#     decodedList = []
#     ptr1 = 0
#     ptr2 = 1

#     while ptr2 < len(s):
#         if s[ptr2] != "#":
#             ptr2 += 1
#         else:
#             parseLen = int(s[ptr1: ptr2])
#             decodedList.append(s[ptr2 + 1: ptr2 + parseLen + 1])
#             ptr1 = ptr2 + parseLen + 1
#             ptr2 = ptr1 + 1
    
#     return decodedList












    #     def encode(self, strs: List[str]) -> str:
    #     encoded = ""

    #     for string in strs:
    #         encoded += str(len(string)) + '#' + string
        
    #     return encoded

    # def decode(self, s: str) -> List[str]:
    #     decodedList, i = [], 0

    #     while i < len(s):
    #         k = i
    #         while s[k] != '#':
    #             k += 1
    #         decodedList.append(s[k + 1: k + 1 + int(s[i:k])])
    #         i = k + 1 + int(s[i:k])
        
    #     return decodedList



