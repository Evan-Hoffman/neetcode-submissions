class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## recognize, for any given substring in s, a valid substution can occur
        ## if len(substring) - count of most frequent char <= k
        ## create a map of character counts, a running max, and a most frquent character tracker 
        ## with a sliding window, starting at 0 to k + 1 length, add the chars to map
        ## caluclate the most frequent, check equation. If less than or equal to K,
        ## add length of substring to max checker, increase window size by 1
        ## if greater than k, increment both pointers

        if len(s) == 1:
            return 1
        if len(s) <= k + 1:
            return len(s)

        counter = {}
        curMax = k + 1
        curMostFreqChar = s[0]

        subString = s[0: k+1]
        for letter in subString:
            counter[letter] = counter.get(letter, 0) + 1
            if letter != curMostFreqChar and counter[letter] > counter[curMostFreqChar]:
                curMostFreqChar = letter

        l = 0
        for r in range(k+1, len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            if s[r] != curMostFreqChar and counter[s[r]] > counter[curMostFreqChar]:
                curMostFreqChar = s[r]
            curLength = r + 1 - l
            if curLength - counter[curMostFreqChar] <= k:
                curMax = max(curMax, curLength)
            else:
                counter[s[l]] -= 1
                l += 1
        
        return curMax
            
                



        