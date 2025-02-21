class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(i, totalsum, path):
            if totalsum == target:
                result.append(path.copy())
                return
            
            if totalsum > target or i >= len(candidates):
                return 
            
            path.append(candidates[i])
            dfs(i+1, totalsum + candidates[i], path)

            path.pop()
            while (i + 1) < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, totalsum, path)
        
        dfs(0, 0, [])
        return result