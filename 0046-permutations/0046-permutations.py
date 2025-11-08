class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def dfs():
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for n in nums:
                if n not in path:
                    path.append(n)
                    dfs()
                    path.pop()

        dfs()
        return result