# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ##using two pointer, right and left, starting at head and head.next
        ##move right over n times
        ##move both pointers till right at the end
        ##remove left.next

        if not head.next:
            return None

        left, right = head, head.next

        while right and n:
            right = right.next
            n -= 1
        
        if n:
            return head.next
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return head

























        # dummy = ListNode(0, head)
        # left, right = dummy, head

        # for i in range(n):
        #     right = right.next
        
        # while right:
        #     right = right.next
        #     left = left.next
        
        # left.next = left.next.next

        # return dummy.next

            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dummy = ListNode(0, head)
        # left, right = dummy, head

        # while n and right:
        #     right = right.next
        #     n -= 1

        # while right:
        #     left = left.next
        #     right = right.next
        
        # left.next = left.next.next

        # return dummy.next
        

        