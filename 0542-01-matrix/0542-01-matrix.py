class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
# If we start BFS from 1, we can only find the shortest distance for that 1. If we start BFS from 0, we could find the shortest distance for many 1 at a time. starting from 1 or 0 both will take x steps, but starting from 0 is efficient

        matrix = mat
        rows, cols = len(mat) , len(mat[0])
        visited = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        
        while queue:
            r, c, level = queue.popleft()

            for dr, dc in [[-1,0], [1,0], [0,-1], [0,1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    matrix[nr][nc] = level + 1
                    queue.append((nr, nc, level +1))
                    visited.add((nr, nc))
        
        return matrix