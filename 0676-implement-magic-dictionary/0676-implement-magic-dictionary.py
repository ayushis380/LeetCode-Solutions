class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur = self.root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.endOfWord = True

    def search(self, searchWord: str) -> bool:
        def dfs(cur, i, changed):
            if i == len(searchWord):
                return changed and cur.endOfWord
            
            ch = searchWord[i]
            
            for key_ch, child in cur.children.items():
                if key_ch == ch:
                    if dfs(child, i+1, changed):
                        return True
                else: # character doesnt match
                    if not changed: # only one change is allowed
                        if dfs(child, i + 1, True):
                            return True

            return False
        
        return dfs(self.root, 0, False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)