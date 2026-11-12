class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.cacheMap = {}
        self.least = Node(0, 0)
        self.most = Node(0, 0)
        self.least.next = self.most
        self.most.prev = self.least
        
        
    def remove(self, node):
        # self.least.next = node.next
        # node.next.prev = self.least

        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev, node.next = None, None
       

    def insert(self, node):
        curFreq = self.most.prev
        curFreq.next = node
        self.most.prev = node
        node.prev, node.next = curFreq, self.most

    def get(self, key: int) -> int:
        if key not in self.cacheMap:
            return -1
        
        node = self.cacheMap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None
        self.insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cacheMap:
            if self.size >= self.cap:
                del self.cacheMap[self.least.next.key]
                self.remove(self.least.next)
            
            newNode = Node(key, value)
            self.cacheMap[key] = newNode
            self.insert(newNode)
            self.size += 1
        
        else:
            node = self.cacheMap[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev, node.next = None, None
            self.insert(node)



       