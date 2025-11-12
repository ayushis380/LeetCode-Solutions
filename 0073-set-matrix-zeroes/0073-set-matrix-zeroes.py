class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()
        m, n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)
        
        for r in range(m):
            for c in range(n):
                if r in row or c in col:
                    matrix[r][c] = 0
        