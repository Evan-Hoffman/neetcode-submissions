class Solution:
    import heapq
    def characterReplacement(self, s: str, k: int) -> int:
        ##add the letters and their counts to a freqs dict
        ##using a sliding window starting len k + 1
        ## increasing the right pointer one at a time, add the letter to the freqs
        ## if most freq <= r - l + 1 - k, we can continue to add, compute the maxwindow
        ## if not ^, increment l and remove the freqs until we satisfy the condition again

        freqs = {}
        maxWindow = 0
        maxFreq = 0
        left = 0

        for right in range(len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freqs[s[right]])

            while k < right - left + 1 - maxFreq:
                freqs[s[left]] -= 1
                left += 1

            maxWindow = max(maxWindow, right - left + 1)
        
        return maxWindow




        