# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            workingList = []
            for i in range(0, len(lists), 2):
                workingList.append(self.mergeSortedLists(lists[i], lists[i + 1] if i < len(lists) - 1 else None))
            
            lists = workingList
        
        return lists[0]

    

    def mergeSortedLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        cur = newHead

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        
        return newHead.next