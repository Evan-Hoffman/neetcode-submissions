class ListNode:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        i = 0
        cur = self.head

        while cur and i < index:
            cur = cur.next
            i += 1
        
        if cur:
            return cur.val

        return -1

        

    def addAtHead(self, val: int) -> None:
        if not self.head:
            newNode = ListNode(val, None, None)
            self.head = newNode
            self.tail = newNode
        
        else:
            curHead = self.head
            self.head = ListNode(val, curHead, None)
            curHead.prev = self.head
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            newNode = ListNode(val, None, None)
            self.head = newNode
            self.tail = newNode

        else:
            curTail = self.tail
            self.tail = ListNode(val, None, curTail)
            curTail.next = self.tail
        
        self.size += 1


        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
            
        elif index == 0:
            self.addAtHead(val)
            return
        
        elif index == self.size:
            self.addAtTail(val)
            return
        
        else:
            i = 0
            cur = self.head

            while cur and i < index:
                cur = cur.next
                i += 1
            
            last = cur.prev
            newNode = ListNode(val, cur, last)
            last.next = newNode
            cur.prev = newNode
        
            self.size += 1
            return
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return

        i = 0
        cur = self.head

        while cur and i < index:
            cur = cur.next
            i += 1
        
        if cur == self.head:
            self.head = self.head.next
            self.head.prev = None
        
        elif cur == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        
        else:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        
        self.size -= 1

            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)