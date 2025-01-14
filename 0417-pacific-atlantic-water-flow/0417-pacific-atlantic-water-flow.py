class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    # updating set for pac, atl is important as it keeps track of valid r,c
    # no need to visit them again        
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        
        def dfs(r, c, visited, prevHt):
            if r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in visited or heights[r][c] < prevHt:
                return
            
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            return

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res