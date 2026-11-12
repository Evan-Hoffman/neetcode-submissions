# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ## create a carry variable and a new head node
        ## using a loop and two pointers, iterate throught the 2 lists while both pointers
            ## add sum + carry as new node
        ## add any carry or extra nodes on either list to the end of new list
        

        prev = ListNode(0)
        head = prev

        carry = 0


        while l1 or l2:
            total = (0 if not l1 else l1.val) + (0 if not l2 else l2.val) + carry

            if total >= 10:
                carry = 1
                total = total % 10
            else:
                carry = 0

            newNode = ListNode(total)

            prev.next = newNode

            prev = prev.next

            # prev = prev.next = newNode

            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next
        
        if carry > 0:
            prev.next = ListNode(carry)
        
        return head.next
        
            

        