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
        newHead = ListNode(0, None)
        prev = newHead
        carry = 0

        while l1 and l2:
            total = l1.val + l2.val + carry
            newVal = total % 10
            carry = total // 10

            newNode = ListNode(newVal, None)
            prev.next = newNode
            prev = prev.next
            l1, l2 = l1.next, l2.next
        
        while l1:
            total = l1.val + carry
            newVal = total % 10
            carry = total // 10

            newNode = ListNode(newVal, None)
            prev.next = newNode
            prev = prev.next
            l1 = l1.next
        
        while l2:
            total = l2.val + carry
            newVal = total % 10
            carry = total // 10

            newNode = ListNode(newVal, None)
            prev.next = newNode
            prev = prev.next
            l2 = l2.next
        
        if carry:
            newNode = ListNode(1, None)
            prev.next = newNode
            prev = prev.next
        
        return newHead.next



        

        

        





























        # prev = ListNode(0)
        # head = prev

        # carry = 0


        # while l1 or l2 or carry:
        #     total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

        #     carry = total // 10
        #     total = total % 10
        
        #     prev.next = ListNode(total)

        #     prev = prev.next
        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None
        
        # return head.next
        
            

        