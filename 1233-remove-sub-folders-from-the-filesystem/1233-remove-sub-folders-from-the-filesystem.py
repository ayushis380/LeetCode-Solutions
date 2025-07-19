class TrieNode():
    def __init__(self):
        self.isEndFolder = False
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        result = []
# Build Trie from folder paths
        for f in folder:
            cur = self.root
            paths = f.split("/")
            
            for p in paths:
                if not p:
                    continue
                if p not in cur.children:
                    cur.children[p] = TrieNode()
                cur = cur.children[p]
        
            cur.isEndFolder = True
        
        # Check each path for subfolders
        for f in folder:
            cur = self.root
            paths = f.split("/")
            isSubFolder = False #  to track if the current path is a sub-folder

            for i, p in enumerate(paths):
                if not p:
                    continue
        # the next node corresponding to the current folder name
                cur = cur.children[p] 
        
    #if nextNode.isEndOfFolder is true and it is not the last folder in the path
                if cur.isEndFolder and i != len(paths) - 1:
                    isSubFolder = True
                    break
            
            if not isSubFolder:
                result.append(f)
        
        return result

