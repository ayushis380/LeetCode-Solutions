class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                result.append(path.copy())
                return
            
            if i >= len(candidates) or total > target:
                return 
            
            path.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, total)
        
        dfs(0, 0)
        return result
            