class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(i, total):
            if total == target:
                result.append(path.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            path.append(candidates[i])
            dfs(i, total + candidates[i])

            path.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return result