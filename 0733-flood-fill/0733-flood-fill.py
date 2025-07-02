class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startcolor = image[sr][sc]
        visited = set()
        rows, cols = len(image), len(image[0])

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or image[r][c] != startcolor or (r, c) in visited:
                return 
            
            image[r][c] = color
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return
        
        dfs(sr, sc)
        return image