class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack)!=self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack)==0:
            return -1
        else:
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        tempStack = []
        while len(self.stack)!=0:
            tempStack.append(self.stack.pop())
        while len(tempStack) and k!=0:
            self.stack.append(tempStack.pop()+val)
            k-=1
        while len(tempStack)!=0:
            self.stack.append(tempStack.pop())


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
