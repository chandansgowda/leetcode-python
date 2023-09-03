class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            oldNode = self.dic[key]
            self.remove(oldNode)
        node = ListNode(key,value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic)>self.capacity:
            lru_node = self.head.next
            self.remove(lru_node)
            del self.dic[lru_node.key]

    def add(self, newNode):
        prev_node = self.tail.prev
        newNode.next = self.tail
        newNode.prev = prev_node
        prev_node.next = newNode
        self.tail.prev = newNode
    
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
