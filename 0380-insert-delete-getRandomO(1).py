class RandomizedSet:

    def __init__(self):
        self.list = []
        self.idx_map = {}
    
    def search(self,val):
        return val in self.idx_map

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        self.list.append(val)
        self.idx_map[val] = len(self.list)-1
        return True
        

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False
        idx = self.idx_map[val]
        self.list[idx] = self.list[-1]
        self.idx_map[self.list[-1]] = idx
        self.list.pop()
        del self.idx_map[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
