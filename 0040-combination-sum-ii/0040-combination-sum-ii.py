class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []

        def backtrack(path, sum, ind):
            if sum == target: # this check is before as we return at len(candidates) if sum matches target
                combinations.append(path.copy())
                return
            if sum > target or ind >= len(candidates):
                return
            
            path.append(candidates[ind])
            backtrack(path, sum+ candidates[ind], ind+1)

            path.pop()
            while ind +1 < len(candidates) and candidates[ind] == candidates[ind+1]:
                ind += 1
            backtrack(path, sum, ind + 1)

        backtrack([], 0, 0)
        return combinations
