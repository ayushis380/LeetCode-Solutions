class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # clockwise 90 degree # first row becomes last column
        matrix.reverse() # 1st row -> last row 

        for i in range(len(matrix)): # last row - > last column by transposing
            for j in range(i+1, len(matrix)): # values at diagonal are same
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # to flip horizontally, along vertical axis
        # for row in matrix:
        #     row.reverse()
        