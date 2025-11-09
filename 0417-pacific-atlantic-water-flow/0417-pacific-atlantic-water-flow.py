class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        result = []
# each ocean has its set - we are trying to see if we can reach from ocean to the cell, cond reversed 
# if we can move from boundaries to inward all the reachable neighbors can be reached from respective ocean     
        def dfs(r, c, prevHt, visited):
            if r >= rows or r < 0 or c >= cols or c < 0 or heights[r][c] < prevHt or (r, c) in visited:
                return 
            
            visited.add((r, c))
            
            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, heights[r][c], visited)

        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols-1], atl)
        
        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows -1][c], atl)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])
        
        return result