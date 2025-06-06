class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # we need to store the values in lexicographical order, so index helps in doing that 
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for ch in word:
            ind = ord(ch) - ord('a')

            if not cur.children[ind]: # if none is at cur.children[ind]
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        
        cur.isWord = True
    
    def dfs(self, node, word):
        if len(self.resultBuffer) == 3:
            return
        
        if node.isWord:
            self.resultBuffer.append(word)
        
        for i in range(26): 
            child = node.children[i] # lexicographical order is maintained as we check words from a to z order
            if child:
                self.dfs(child, word + chr(ord('a') + i)) # keep on building the word
    

    def getWordsStartWith(self, prefix): # go till the prefix node and then do dfs
        cur = self.root
        self.resultBuffer = []

        for ch in prefix:
            ind = ord(ch) - ord('a')
            if not cur.children[ind]:
                return [] # if unable to reach prefix then just return 
            cur = cur.children[ind]
        
        self.dfs(cur, prefix) # reached prefix node, now look for words which start from cur. We need prefix to build the result
        return self.resultBuffer
    

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()

        for p in products: # insert all products in trie
            trie.insert(p)
        
        result = []
        prefix = ""
        
        for ch in searchWord:
            prefix += ch # keep on building prefix 
            result.append(trie.getWordsStartWith(prefix))
        
        return result