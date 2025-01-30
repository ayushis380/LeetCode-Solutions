class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def countDistinct(self, s: str) -> int:
        root = TrieNode()
        count = 0

        for i in range(len(s)):
            cur = root
            for j in range(i, len(s)):
                ch = s[j]
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                    count += 1
                cur = cur.children[ch]
        
        return count