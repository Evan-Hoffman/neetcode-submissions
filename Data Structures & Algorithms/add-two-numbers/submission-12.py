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
        
        carry = 0
        newHead = ListNode()
        cur = newHead
        
        while carry or l1 or l2:
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = total // 10
            toAdd = ListNode(total % 10)
            cur.next = toAdd
            cur, l1, l2 = cur.next, l1.next if l1 else None, l2.next if l2 else None
        
        
        return newHead.next
            


        

            

        