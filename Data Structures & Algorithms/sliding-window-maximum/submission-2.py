class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ## create an empty dequeue. It will maintain non-increasing order (max always at front)
        ##for 0 to k:
            ## while the tail of the deque is smaller than element, pop the tail
            ## insert the element at the tail
        
        ##declare left pointer at 0, empty results array
        ##for right in range(k, len(nums)):
            ## add head of dequeue to results array
            ## identify element to remove, nums[left]
                ## if the head of the array is this element, pop the head
            ##identify element to add, nums[right]:
                 ## while the tail of the deque is smaller than element, pop the tail
                 ## insert the element at the tail
        
        elements = deque()
        
        left = 0
        results = []

        for right in range(len(nums)):
            while elements and elements[-1] < nums[right]:
                elements.pop()
            elements.append(nums[right])

            if right + 1 >= k:
                results.append(elements[0])
                toRem = nums[left]
                if elements[0] == toRem:
                    elements.popleft()
                left += 1            
        
        return results
                

        
        