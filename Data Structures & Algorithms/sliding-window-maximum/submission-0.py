class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ## add the numbers in the initial window to a deque, decreasing order
        ## each iteration
        deque = []
        results = []

        l = 0

        for r in range(len(nums)):
            while len(deque) and nums[deque[-1]] < nums[r]:
                deque.pop()
            deque.append(r)

            if l > deque[0]:
                deque = deque[1:]
            
            if (r + 1) >= k:
                results.append(nums[deque[0]])
                l += 1
        
        return results



        
        return results


            


        