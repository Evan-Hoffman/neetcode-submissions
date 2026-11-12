class Solution:
    import heapq
    def characterReplacement(self, s: str, k: int) -> int:
        ## keep a counter, maxWindow, maxFreq
        ##using a sliding window with pointers left and right
            ## increasing the right pointer one at a time, add the letter to the freqs
            ## keep of amount of count of most freq char in maxFreq
            ## while k is smaller than the differene of the size of the window minus the count of the most freq char, we need to shrink our window
                # increment l and remove the freqs until we satisfy the condition
            ## compare the window to the maxWindow

        freqs = {}
        maxWindow = 0
        left = 0
        maxFreq = 0
        
        for right in range(0, len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freqs[s[right]])
            
            while k < right - left + 1 - maxFreq:
                freqs[s[left]] -= 1                    
                left += 1
            
            maxWindow = max(maxWindow, right - left + 1)
        
        return maxWindow



        