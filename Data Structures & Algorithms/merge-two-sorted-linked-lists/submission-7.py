# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = ListNode(0, list1), ListNode(0, list2)
        head = l1

        while (l1.next and l2.next):
            if l1.next.val <= l2.next.val:
                l1 = l1.next
            else:
                temp1 = l1.next
                temp2 = l2.next
                l2 = ListNode(0, temp2.next)
                l1.next = temp2
                l1.next.next = temp1
                l1 = l1.next
        
        if l2.next:
            l1.next = l2.next
        
        return head.next



        