class Solution:
    import heapq
    def characterReplacement(self, s: str, k: int) -> int:
        ##add the letters and their counts to a freqs dict
        ##using a sliding window starting len k + 1
        ## increasing the right pointer one at a time, add the letter to the freqs
        ## if most freq <= r - l + 1 - k, we can continue to add, compute the maxwindow
        ## if not ^, increment l and remove the freqs until we satisfy the condition again
        if len(s) <= k + 1:
            return len(s)

        freqs = {}
        maxWindow = k + 1

        for letter in s[0: k + 1]:
            freqs[letter] = freqs.get(letter, 0) + 1
        
        left = 0
        for right in range(k + 1, len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            while k < right - left + 1 - self.getMax(freqs)[1]:
                toRem = freqs.get(s[left], 0)
                if toRem == 1:
                    freqs.pop(s[left])
                else:
                    freqs[s[left]] = freqs.get(s[left], 0) - 1
                left += 1

            maxWindow = max(maxWindow, right - left + 1)
        
        return maxWindow

    def getMax(self, freqs) -> (str, int):
        curMax = 0
        curMaxLetter = None
        for key, val in freqs.items():
            if val > curMax:
                curMax = val
                curMaxLetter = key
        
        return (curMaxLetter, curMax)




        