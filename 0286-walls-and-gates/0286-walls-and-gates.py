class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c, 0))
        
        while queue:
            r, c, dist = queue.popleft()
            for dr, dc in [[-1,0], [1,0], [0,1], [0,-1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                    queue.append((nr, nc, dist + 1))
                    rooms[nr][nc] = dist + 1