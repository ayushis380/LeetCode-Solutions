class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # add all words to trie
        root = TrieNode()
        for wrd in words:
            cur = root
            for ch in wrd:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.endOfWord = True
        
        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, cur, wrd):
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] not in cur.children or board[r][c] == "#":
                return 
            
            ch = board[r][c]
            next_node = cur.children[ch]
            wrd += ch
            board[r][c] = "#"

            if next_node.endOfWord:
                result.append(wrd)
                next_node.endOfWord = False # avoid duplicates

            dfs(r + 1, c, next_node, wrd)
            dfs(r - 1, c, next_node, wrd)
            dfs(r, c - 1, next_node, wrd)
            dfs(r, c + 1, next_node, wrd)

            board[r][c] = ch
            
            if not next_node.children: # prune if next node doesn't have any children
        # eg in oath, when at "h" - no children then t.children[h] is deleted as "h" is leaf node and wont be used again
                del cur.children[ch] 

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        # def print_trie(node, prefix=""):
        #     if node.endOfWord:
        #         print(f"'{prefix}' (end)")
        #     for ch, child in node.children.items():
        #         print_trie(child, prefix + ch)
        
        # print_trie(root)
        return result
