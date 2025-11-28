from collections import defaultdict
class RandomizedSet:

    def __init__(self):
        self.hmap = defaultdict(int)
        self.hlist = []

    def insert(self, val: int) -> bool:
        if val not in self.hmap:
            self.hmap[val] = len(self.hlist)
            self.hlist.append(val)
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.hmap:
            ind = self.hmap[val]
            lastVal = self.hlist[-1]

            self.hmap[lastVal] = ind
            self.hlist[ind] = lastVal
            self.hlist.pop()
            del self.hmap[val]
            
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.hlist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()