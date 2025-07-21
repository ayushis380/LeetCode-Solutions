class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        
        cur.end = True

    def search(self, word: str) -> bool:

        def dfs(i, root):
            cur = root
            
            for j in range(i, len(word)):
                ch = word[j]

                if ch == ".":
                    for child in cur.children.values(): # need to explore all children of cur
                        if dfs(j + 1, child): # if . then do dfs()
                            return True # if any yield True then return 
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch] # next children of cur, checked within same for loop, dfs() not required
            
            return cur.end # once the length is reached, end depicts if the word is present or not

        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)