# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        size = 0

        while tail:
            size += 1
            tail = tail.next
        
        if size == n:
            return head.next
        
        cur = head
        
        for i in range(size - n -1):
            cur = cur.next
        
        cur.next = cur.next.next

        return head

            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        

        