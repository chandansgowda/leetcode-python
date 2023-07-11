class RandomizedSet:

    def __init__(self):
        self.m = {}
        self.data = []
        
    def insert(self, val: int) -> bool:
        if val in self.m:
            return False
        else:
            self.m[val]=len(self.data)
            self.data.append(val)
            return True
        
    def remove(self, val: int) -> bool:
        if val not in self.m: 
            return False
        else:
            val_pos= self.m[val]
            self.m[self.data[-1]] = val_pos
            self.data[val_pos], self.data[-1] = self.data[-1], self.data[val_pos]
            self.m.pop(val)
            self.data.pop()
            return True

    def getRandom(self) -> int:
        return random.choice(self.data)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
