class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.updatePlace(node)
            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.updatePlace(node)
            node.val = value

        else:
            if len(self.cache) == self.cap:
                leastUsedNode = self.left.next
                leastUsedNode.next.prev = self.left
                self.left.next = leastUsedNode.next
                self.cache.pop(leastUsedNode.key)

            newNode = Node(key, value, self.right, self.right.prev)
            self.right.prev.next = newNode
            self.right.prev = newNode
            self.cache[key] = newNode
    
    def updatePlace(self, node: Node) -> None:            
        tempLeft = node.prev
        tempLeft.next = node.next
        tempLeft.next.prev = tempLeft

        tempPrev = self.right.prev
        tempPrev.next = node
        node.prev = tempPrev
        node.next = self.right
        self.right.prev = node            



        



        
