"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        oldToNew = {None: None}

        newHead = Node(head.val)

        curOld = head
        curNew = newHead

        while curOld.next:
            curNew.val = curOld.val
            curNew.next = Node(0)
            curNew.random = curOld.random

            oldToNew[curOld] = curNew
            curOld = curOld.next
            curNew = curNew.next
        
        curNew.val = curOld.val
        curNew.next = None
        curNew.random = curOld.random
        oldToNew[curOld] = curNew
        
        cur = newHead

        while cur:
            cur.random = oldToNew[cur.random]
            cur = cur.next
        
        return newHead
        

            
        

        