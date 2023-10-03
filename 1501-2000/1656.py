class OrderedStream:

    def __init__(self, n: int):
        self.data = [None]*n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey-=1
        self.data[idKey]=value
        
        if idKey>self.ptr: 
            return []

        while self.ptr < len(self.data) and self.data[self.ptr]:
            self.ptr+=1
        return self.data[idKey:self.ptr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
