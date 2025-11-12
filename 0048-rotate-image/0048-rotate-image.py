class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        for i in range(m//2):
            tmp = matrix[i]
            matrix[i] = matrix[m - i -1]
            matrix[m -i - 1] = tmp
        
        # print(matrix)
        for i in range(m):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        