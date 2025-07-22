class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        
        while queue:
            r, c, dist = queue.popleft()
            for dr, dc in [[-1,0], [1, 0], [0,1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    queue.append((nr, nc, dist + 1))
                    visited.add((nr, nc))
                    mat[nr][nc] = dist + 1
        
        return mat