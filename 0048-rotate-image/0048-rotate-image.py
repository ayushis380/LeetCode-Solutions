class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Reverse the matrix vertically
        matrix.reverse()

# inner loop starts the j index from i + 1 in the transpose step of the rotate method is to ensure that each element in the matrix is swapped only once and to avoid redundant swaps

        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            