class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]] 
        
        perms = self.permute(nums[1:]) # nums[0] will be inserted in this 2D list
        res = []
        for p in perms: # for all perms we need to insert nums[0] in p's range 
            for i in range(len(p) +1): # value can be inserted at end - so +1 
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res