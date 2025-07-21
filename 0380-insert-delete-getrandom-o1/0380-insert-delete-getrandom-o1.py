class RandomizedSet:

    def __init__(self):
        self.hashlist = []
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashlist.append(val)
            self.hashmap[val] = len(self.hashlist) - 1
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            ind = self.hashmap[val]
            lastVal = self.hashlist[-1]

            self.hashlist[ind] = lastVal
            self.hashmap[lastVal] = ind
            self.hashlist.pop()
            del self.hashmap[val]
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.hashlist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()