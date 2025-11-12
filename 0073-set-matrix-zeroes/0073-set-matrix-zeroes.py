class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        firstRow = any(matrix[0][c] == 0 for c in range(n))
        firstCol = any(matrix[r][0] == 0 for r in range(m))

        # if any of (1, m) and (1, n) values are 0
        # use 0th row and 0th col to flag 0 values in the rest of the array
        for r in range(1, m): 
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, m): # mark everything to 0 
            for c in range(1, n): 
                if matrix[0][c] == 0:
                    matrix[r][c] = 0
                if matrix[r][0] == 0:
                    matrix[r][c] = 0
        # if any of the values in 0th row is 0, then entire 0th row needs to be marked to 0
        # done at end as if we mark 0th row in start then it will impact the other cells in matrix
        # they are the indicators for the other values in matrix
        if firstRow: 
            for c in range(n):
                matrix[0][c] = 0
        
        if firstCol:
            for r in range(m):
                matrix[r][0] = 0
