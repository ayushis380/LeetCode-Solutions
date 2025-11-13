class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        
        cur.endOfWord = True
        
    def search(self, word: str) -> bool:
        
        def dfs(i, root):
            cur = root
            for j in range(i, len(word)):
                ch = word[j]
                if ch == ".":
                    for v in cur.children.values():
                        if dfs(j + 1, v):
                            return True
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            
            return cur.endOfWord # this is imp, we dont put a check on the length of word(if i has reached end) as word might not be a part of Trie
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)