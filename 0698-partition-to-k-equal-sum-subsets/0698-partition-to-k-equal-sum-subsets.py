class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k: # unable to divide into k subsets
            return False
        
        target = total//k
        n = len(nums)
        nums.sort(reverse= True)

        @lru_cache(None) # memoiz function calls, backtrack(used, current_sum, subsets_filled) with same set of values could be called many times so cache it
        def backtrack(used, current_sum, subsets_filled):
            if subsets_filled == k:
                return True # all formed
            
            if current_sum == target: # formed one subset
                return backtrack(used, 0, subsets_filled + 1) # start searching again
            
            for i in range(n):
                # 1 << i : 1 << 1 = 0000010 creates a mask with only the i-th bit set 
                # bitwise and op checks if at index i, value is 1 or not - 1 means already used

                if ((used & 1 << i) or current_sum + nums[i] > target):
                    continue # when value from nums is already used or sum exceeds 
                
                # Mark nums[i] as used by setting the bit at index i, bitwise or
                # (used | 1 << i) makes sure we dont have to unset used after each call as its a backtracking
                if backtrack((used | 1 << i), current_sum + nums[i], subsets_filled):
                    return True # Found a valid partition
            
            return False
        
        return backtrack(0, 0, 0)
            

        

