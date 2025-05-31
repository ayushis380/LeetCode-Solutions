class MyHashSet:
# O(N/ K), where N is the number of all possible values and K is the number of predefined buckets
# SC: O(K+M) where K is the number of predefined buckets, and M is the number of unique values that have been inserted into the HashSet
    
    def __init__(self):
        self.keyRange = 769
        self.bucketLL = [Bucket() for i in range(self.keyRange)] # array of buckets
    
    def _hash(self, key):
        return key % self.keyRange

    def add(self, key: int) -> None:
        index = self._hash(key)
        self.bucketLL[index].insert(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        self.bucketLL[index].delete(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return self.bucketLL[index].exists(key)

class Node:
    def __init__(self, value, nextNode= None):
        self.value = value
        self.next = nextNode

class Bucket:
    def __init__(self):
        self.head = Node(0)
    
    def insert(self, newValue):
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next) # make the old head.next as new Node's next
            self.head.next = newNode # inserting at the head 
    
    def delete(self, value):
        prev = self.head
        curr = self.head.next

        while curr:
            if curr.value == value:
                prev.next = curr.next
                return
            
            prev = curr
            curr = curr.next
    
    def exists(self, value):
        curr = self.head.next

        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)