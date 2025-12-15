class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n  for i in range(n)]
        col, posd, negd = set(), set(), set()
        result = []

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n): # at every row explore all the columns
                if c not in col and (r + c) not in posd and (r - c) not in negd:
                    board[r][c] = "Q"
                    col.add(c)
                    posd.add(r + c)
                    negd.add(r - c)
                    dfs(r + 1)

                    col.remove(c)
                    posd.remove(r + c)
                    negd.remove(r - c)
                    board[r][c] = "."
        
        dfs(0)
        return result
