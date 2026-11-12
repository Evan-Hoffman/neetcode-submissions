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
        #create a map of old node to new node
        # add every node in original to map, mapping to empty new node
        # iterate through first list, and properly set nexts and randoms in map
    
        oldToNew = {None: None}

        cur = head

        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            oldToNew[cur].next = oldToNew[cur.next]
            oldToNew[cur].random = oldToNew[cur.random]
            cur = cur.next
        
        return oldToNew[head]


















        # cur = head

        # oldToNew = {None : None}

        # while cur:
        #     oldToNew[cur] = Node(cur.val)
        #     cur = cur.next
        
        # cur = head
        # while cur:
        #     oldToNew[cur].next = oldToNew[cur.next]
        #     oldToNew[cur].random = oldToNew[cur.random]
        #     cur = cur.next
        
        # return oldToNew[head]
        









        


























        # oldToNew = collections.defaultdict(lambda: Node(0))
        # oldToNew[None] = None

        # cur = head

        # while cur:
        #     oldToNew[cur].val = cur.val
        #     oldToNew[cur].next = oldToNew[cur.next]
        #     oldToNew[cur].random = oldToNew[cur.random]

        #     cur = cur.next
        
        # return oldToNew[head]
        

            
        

        