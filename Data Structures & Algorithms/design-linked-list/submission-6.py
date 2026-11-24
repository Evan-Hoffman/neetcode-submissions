class ListNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        i = -1
        cur = self.head

        while cur != self.tail and i < index:
            cur = cur.next
            i += 1
        
        if cur != self.tail:
            return cur.val

        return -1

        

    def addAtHead(self, val: int) -> None:
        prevHead = self.head.next
        self.head.next = ListNode(val, self.head, prevHead)
        prevHead.prev = self.head.next

    def addAtTail(self, val: int) -> None:
        prevTail = self.tail.prev
        self.tail.prev = ListNode(val, prevTail, self.tail)
        prevTail.next = self.tail.prev
    

    def addAtIndex(self, index: int, val: int) -> None:
        i = -1
        cur = self.head

        while cur != self.tail and i < index:
            cur = cur.next
            i += 1
        
        if i == index:
            before = cur.prev
            newNode = ListNode(val, before, cur)
            cur.prev = newNode
            before.next = newNode
        
        
    def deleteAtIndex(self, index: int) -> None:
        i = -1
        cur = self.head

        while cur != self.tail and i < index:
            cur = cur.next
            i += 1

        if cur != self.tail:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)