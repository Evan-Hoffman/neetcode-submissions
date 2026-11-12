class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}

        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
        
        for char in t:
            if char not in counter:
                return False
            if counter[char] == 1:
                counter.pop(char)
            else:
                counter[char] -= 1
        
        return len(counter) == 0;
        