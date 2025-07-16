class FileSystem:

    def __init__(self):
        self.paths = defaultdict(list)
        self.files = defaultdict(str)

    def ls(self, path: str) -> List[str]:
        if path in self.files:
            return [path.split("/")[-1]] # return list 
        else:
            return self.paths[path]
        

    def mkdir(self, path: str) -> None:
        dirc = path.split("/")
        
        for i in range(1, len(dirc)):
            cur = "/".join(dirc[:i]) or "/"

            if cur not in self.paths or dirc[i] not in self.paths[cur]:
                bisect.insort(self.paths[cur], dirc[i])
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.files:
            self.mkdir(filePath)
        
        self.files[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)