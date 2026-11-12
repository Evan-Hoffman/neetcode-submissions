class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        counts = {}

        for phrase in strs:
            ascii_array = [0] * (ord("z") - ord("a"))

            for char in phrase:
                ascii_array[ord(char) - ord("a")] += 1
            
            as_tuple = tuple(ascii_array)
            if as_tuple in counts:
                counts[as_tuple] = counts.get(as_tuple, []) + [phrase]
            else:
                counts[as_tuple] = [phrase]

        return counts.values()
        