class FileSystem:

    def __init__(self):
        self.paths = defaultdict(list) # path - > list of filenames and dir under that path 
        self.files = defaultdict(str) # filename -> content (in str)
        

    def ls(self, path: str) -> List[str]:
        if path in self.files: # if path is a file path then return the file name
            return [path.split("/")[-1]] # eg a/b/c/d.js
        else:
            return self.paths[path]

    def mkdir(self, path: str) -> None:
        directories = path.split("/") 

        # there can be middle directories that aren't made, so check that
        # /a/b = splitiing this gives ["","a","b"], so start range from 1

        for i in range(1, len(directories)):
            cur = "/".join(directories[:i]) or "/"
            
            # if cur is not defined or sub directory is not in current path
            if cur not in self.paths or directories[i] not in self.paths[cur]:
                bisect.insort(self.paths[cur], directories[i]) # inserts in lexicographic order, or use binary search to insert at correct position
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.files:
            self.mkdir(filePath)
        
        self.files[filePath] += content # append the content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)