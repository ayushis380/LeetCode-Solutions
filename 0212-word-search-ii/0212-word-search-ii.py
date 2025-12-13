class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        rows, cols = len(board), len(board[0])
        result = []

        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            
            cur.endOfWord = True
        
        def dfs(cur, r, c, word): # cur start from root
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] not in cur.children:
                return
            
            ch = board[r][c]
            board[r][c] = "#"
            word += ch
            cur = cur.children[ch]
            
            if cur.endOfWord:
                result.append(word)
                cur.endOfWord = False

            for dr, dc in [[-1,0], [1,0], [0,-1], [0,1]]:
                nr, nc = r + dr, c + dc
                dfs(cur, nr, nc, word)

            board[r][c] = ch
        
        # print(root.children.items())

        for r in range(rows):
            for c in range(cols):
                dfs(root, r, c, "")
        
        return result