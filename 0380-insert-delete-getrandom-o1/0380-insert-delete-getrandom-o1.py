class RandomizedSet:

    def __init__(self):
    # HashSet can't be used - we cant index a hash set
    # as the values are stored in random order, wont be able to fetch through an index

        self.numMap = {} # val -> index (where its stored in numList)
        self.numList = [] 
        

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numMap)
            self.numList.append(val)
        
        return res
        

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        # removing the element from a list is difficult as it needs adjusting costing O(n) 
        # so remove the last element from list as it O(1)
        # removed last element will be placed at val's index - dont forget to update the map as it stores the index of last val

        if res:
            idx = self.numMap[val] # index of element to be removed
            lastVal = self.numList[-1] # last val
            self.numList[idx] = lastVal # place last val at idx (val's index)
            self.numMap[lastVal] = idx # update index in map
            self.numList.pop() # remove last element
            del self.numMap[val]
        
        return res


    def getRandom(self) -> int:
        return random.choice(self.numList) # remaining elements have same probability 
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()