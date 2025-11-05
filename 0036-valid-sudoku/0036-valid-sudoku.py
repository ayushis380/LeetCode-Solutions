class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                if val in row[r] or val in col[c] or val in grid[(r//3, c//3)]:
                    return False
                
                row[r].add(val)
                col[c].add(val)
                grid[(r//3, c//3)].add(val)
        
        return True