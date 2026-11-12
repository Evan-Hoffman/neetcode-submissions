class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = {}
        ascii_a = ord("a")

        for phrase in strs:
            emptyAlpha = [0] * 26
            for c in phrase:
                ascii_char = ord(c) - ascii_a
                emptyAlpha[ascii_char] += 1
            
            asTuple = tuple(emptyAlpha)
            if asTuple in anaMap:
                anaMap[asTuple].append(phrase)
            else:
                anaMap[asTuple] = [phrase]
        
        return [group for group in anaMap.values()]






























        # anaCounter = {}

        # for phrase in strs:
        #     emptyAlpha = [0] * 26

        #     for char in phrase:
        #         ascii = ord(char) - ord('a')
        #         emptyAlpha[ascii] += 1
            
        #     asTuple = tuple(emptyAlpha)
        #     if asTuple in anaCounter:
        #         anaCounter[asTuple].append(phrase)
        #     else:
        #         anaCounter[asTuple] = [phrase]
        
        # return anaCounter.values()