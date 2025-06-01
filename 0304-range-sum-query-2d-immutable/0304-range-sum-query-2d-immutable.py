class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
 # an extra row above and extra col on left for simplication - this matrix is store the prefix sum 
        self.sumMat = [[0] * (cols + 1) for i in range(rows + 1)]
    # prefix sum by rows is stored 
    # above is for row above the current one 
    # summing them gives the total sum of grid, eg (3,4) in sumMat will give sum of all elements from (0,0) to (3,4) index

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1] # sumMat indexes are +1 as comapred to matrix, so self.sumMat[r + 1 -1][c + 1] = self.sumMat[r][c + 1]. above is to capture the prefix sum of row above r 
                self.sumMat[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1 # extra row and col in sumMat

        bottomRight = self.sumMat[row2][col2] # this has total sum of the grid from (0,0) to (row2, col2)
        topRight = self.sumMat[row1 - 1][col2] # prefix sum stored in (row1 + 1 - 1) - has sum of all rows above it
        bottomLeft = self.sumMat[row2][col1 - 1] # prefix sum of leftmost columun - has sum of values above
        topLeft = self.sumMat[row1 -1][col1 - 1] # this is considered twice in subtraction as its a part of topright and bottomleft

        return bottomRight - topRight - bottomLeft + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)