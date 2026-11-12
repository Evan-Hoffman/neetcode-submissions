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
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

            carry = total // 10
            total = total % 10
        
            newNode = ListNode(total)

            prev.next = newNode

            prev = prev.next

            # prev = prev.next = newNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry > 0:
            prev.next = ListNode(carry)
        
        return head.next
        
            

        