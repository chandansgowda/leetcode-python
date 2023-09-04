class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insertHead(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
        self.size+=1

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lfuFreq = 0
        self.freqTable = collections.defaultdict(DLL)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        return self.updateCache(self.cache[key], self.cache[key].val)
        

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        if key in self.cache:
            self.updateCache(self.cache[key], value)
        else:
            if len(self.cache) == self.capacity:
                prevTail = self.freqTable[self.lfuFreq].removeTail()
                del self.cache[prevTail.key]
            node = ListNode(key, value)
            self.freqTable[1].insertHead(node)
            self.cache[key] = node
            self.lfuFreq = 1
    
    def updateCache(self, node, value):
        node.val = value
        prevFreq = node.freq
        node.freq += 1
        self.freqTable[prevFreq].removeNode(node)
        self.freqTable[node.freq].insertHead(node)
        if prevFreq == self.lfuFreq and self.freqTable[prevFreq].size==0:
            self.lfuFreq += 1
        return node.val      


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
