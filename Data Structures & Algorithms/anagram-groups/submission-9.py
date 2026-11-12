class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        offset = ord('a')
        anagrams = defaultdict(list)
        
        for word in strs:
            char_counts = [0] * 26

            for char in word:
                index = ord(char) - offset
                char_counts[index] += 1
            
            as_tuple = tuple(char_counts)

            anagrams[as_tuple].append(word)
                    
        return list(anagrams.values())