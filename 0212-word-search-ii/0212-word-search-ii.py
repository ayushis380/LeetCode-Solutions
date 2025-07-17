class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        result = []

        # Build Trie
        for w in words:
            cur = self.root
            for ch in w:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.endOfWord = True

        def dfs(r, c, cur, w):
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] not in cur.children:
                return

            ch = board[r][c]
            w += ch
            next_node = cur.children[ch]
            board[r][c] = "#"

            if next_node.endOfWord:
                result.append(w)
                next_node.endOfWord = False  # Avoid duplicates

            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, next_node, w)

            board[r][c] = ch

            # PRUNING STEP: If no children left after DFS, remove this node
            if not next_node.children:
                del cur.children[ch]

        # Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, self.root, "")

        return result
