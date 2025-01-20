class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    # need to focus on indexes, higher chances to get it wrong
    # keeping right and bottom at +1 than required to fit the range func
    # dont forget to update the indexes when accessing the value
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        output = []

        while left < right and top < bottom:
            for i in range(left, right):
                output.append(matrix[top][i]) # same row, col changing
            top += 1

            for i in range(top, bottom):
                output.append(matrix[i][right - 1]) # same col, row changing
            right -= 1
        
        # eg 1 2 3 or 1 \n 2 \n 3
        # top and right values are updated so need to check again if they are in boundaries
            if not( left < right and top < bottom ): 
                break
            
            for i in range(right - 1, left - 1, -1):
                output.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                output.append(matrix[i][left])
            left += 1
        
        return output
