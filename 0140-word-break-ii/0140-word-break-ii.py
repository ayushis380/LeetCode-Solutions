class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        
        cur.endOfWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Trie implementation - check possible words s in reverse
        # to compare them to the wordDict
        trie = Trie()
        dp = {}
        for word in wordDict:
            trie.insert(word)
        
        n = len(s)
        for start in reversed(range(n)): # at every start ind from reverse
            valid = []
            cur = trie.root
            for end in range(start, n): # start to n
                ch = s[end]
                if ch not in cur.children:
                    break
                
                cur = cur.children[ch]
                if cur.endOfWord: # present in trie
                    word = s[start : end + 1]
                    if end == n -1: # reached end, so full word needs to be appended
                        valid.append(word)
                    else:
                        sentences_next = dp.get(end + 1, []) # form full string from the old values in dp
                        for sntc in sentences_next:
                            valid.append(word + " " + sntc) # word comes before the existing values as its in reverse

            dp[start] = valid # store formed words/sentences
        
        return dp.get(0, []) # index 0 will have all valid sentences
                
