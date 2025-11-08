class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        arr = self.permute(nums[1:])
        result = []
        
        for ls in arr:
            for i in range(len(ls) + 1):
                cpy = ls.copy() # for every value in ls, a copy a created to insert nums[0]
                cpy.insert(i, nums[0])
                result.append(cpy)
        
        return result


