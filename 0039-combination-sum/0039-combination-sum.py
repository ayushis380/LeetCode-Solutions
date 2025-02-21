class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        path = []

        def dfs(totalsum, i):
            if totalsum == target:
                combinations.append(path.copy())
                return

            if totalsum > target or i >= len(candidates):
                return
            
            # here totalsum is unchanged, we are adding a value to it
            path.append(candidates[i])
            dfs(totalsum + candidates[i], i)

            path.pop()
            dfs(totalsum, i+1) # as totalsum is unchanged so need to substract candidates[i] from it
        
        dfs(0,0)

        return combinations