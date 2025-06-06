class FileSystem:

    def __init__(self):
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths:
            return False

        parent = path[:path.rfind('/')] # check that the immediate parent path exists — not all previous segments. This is done by finding the last / and checking if the parent path is in the paths dictionary. For path "/a/b", you must ensure "/a" exists
        print(path.rfind('/')) # gives index of last '/
        if parent and parent not in self.paths:
            return False
        
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)