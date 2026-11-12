# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ##find the second half of the list
        ## reverse the second half of the list
        ## add the nodes from the first and second list one at a time

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next        
        slow.next = None
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        secondHead = prev

        

        while head and secondHead:
            temp1, temp2 = head.next, secondHead.next
            head.next = secondHead
            secondHead.next = temp1
            head, secondHead = temp1, temp2
            
        

            





























        # slow, fast = head, head.next

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        
        # second = slow.next
        # prev = slow.next = None

        # while second:
        #     temp = second.next
        #     second.next = prev
        #     prev = second
        #     second = temp
        
        # first, second = head, prev

        # while first and second:
        #     temp1, temp2 = first.next, second.next
        #     first.next = second
        #     second.next = temp1
        #     first, second = temp1, temp2




        



        