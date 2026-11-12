class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        anagrams = {}

        for phrase in strs:
            alphabet = [0] * 26

            for char in phrase:
                ascii = ord(char) - ord('a')
                alphabet[ascii] += 1

            asTuple = tuple(alphabet)

            if asTuple in anagrams:
                anagrams[asTuple].append(phrase)
            else:
                anagrams[asTuple] = [phrase]
        
        return anagrams.values()
        