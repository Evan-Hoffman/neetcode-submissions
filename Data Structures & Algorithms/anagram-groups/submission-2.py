class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        ascii_a = ord("a")

        for str in strs:
                emptyAlphabet = [0] * 26

                for char in str:
                    emptyAlphabet[ord(char) - ascii_a] += 1
                
                as_tuple = tuple(emptyAlphabet)

                if as_tuple in results:
                    results[as_tuple].append(str)
                else:
                    results[as_tuple] = [str]
                
                #results[tuple(emptyAlphabet)].append(str)

        return results.values()
        # if len(strs) == 1:
        #     return [strs]

        # phrases_map = defaultdict(list)

        # for phrase in strs:
        #     ascii_array = [0] * (ord("z") - ord("a"))

        #     for character in phrase:
        #         ascii_value = ord(character) - ord("a")
        #         ascii_array[ascii_value] += 1

        #     as_tuple = tuple(ascii_array)

        #     phrases_map[as_tuple].append(phrase)
 
        
        # return phrases_map.values()

        