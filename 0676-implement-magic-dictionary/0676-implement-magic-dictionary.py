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

        def dfs(node, i, changed):
            if i == len(searchWord):
                return changed and node.endOfWord # lengths should match eg leetcode and leetcoded
            
            ch = searchWord[i]
            
            for child_char, child in node.children.items():
                if child_char == ch:
                    if dfs(child, i + 1, changed):
                        return True
                else:
                    if not changed:
                        if dfs(child, i + 1, True):
                            return True
            return False

        return dfs(self.root, 0, False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)