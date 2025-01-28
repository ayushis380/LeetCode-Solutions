class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    # Instead of starting BFS from 1, start from 0
    # think when entire matrix is 1 except for corners with 10,000 cells = 10^8 TC 
    # starting from 0 will give the same distance in an efficient way
    # multi level BFS

        matrix = mat # taking a copy, generally not considered good practice to modify the input, especially for arrays as they are passed by reference
        queue = deque()
        rows, cols = len(mat), len(mat[0])
        visited = set() # we wont be visiting a cell twice, so O(m * n ) TC

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 0)) # 0 is the step, level 0 of BFS
                    visited.add((r, c))
        
        while queue:
            r, c, steps = queue.popleft()
            for dr, dc in [[-1,0], [1,0], [0,1], [0,-1]]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    matrix[nr][nc] = steps + 1 # updating the steps in copy matrix
                    queue.append((nr, nc, steps + 1))
                    visited.add((nr, nc))
        
        return matrix