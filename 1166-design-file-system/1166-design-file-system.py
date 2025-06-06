class TrieNode:
    def __init__(self, name):
        self.map = defaultdict(TrieNode)
        self.value = -1
        self.name = name # sub file path name

class FileSystem:

    def __init__(self):
        self.root = TrieNode("") # start with empty root

    def createPath(self, path: str, value: int) -> bool:
        # It takes O(T) to add a path to the trie if it contains T components

        cur = self.root # all are types of TrieNode 
        components = path.split("/")

        for i in range(1, len(components)): # go through all
            name = components[i]

            if name not in cur.map:
                if i == len(components) - 1: # if last sub path then that means create a new path for it 
                    cur.map[name] = TrieNode(name) # Adds it to the current node's child map (cur.map) under key name
                else: 
                    return False # parent paths doenst exist
            cur = cur.map[name]
        
        if cur.value != -1: # path already present
            return False
        
        cur.value = value # set the value
        return True

    def get(self, path: str) -> int:
        # takes O(T) to find a path in the trie if it contains T components.
        cur = self.root
        components= path.split("/")

        for i in range(1, len(components)):
            name = components[i]

            if name not in cur.map:
                return -1
            cur = cur.map[name]
        
        return cur.value
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)