class Solution:
    def canJump(self, nums: List[int]) -> bool:
    # DP 
        dp = [-1] * len(nums) # a position can be -1 unknown, 0 bad, 1 good
        dp[-1] = 1 # last index can reach itself so a good one

        def dfs(i):
            if dp[i] != -1:
                return dp[i] == 1
            
            # furthest jump from that index, compare with length as first param of min 
            # can go out of bound
            furthestJump = min(i + nums[i], len(nums) - 1)
            # check for all next pos that can be reached from i
            for nextposition in range(i+1, furthestJump+1):
                if dfs(nextposition): # if able to reach the last index then True
                    dp[i] = 1 # means we can reach the last index
                    return True # we need to check once if possible to reach end
            
            dp[i] = 0 # bad pos as cant reach end
            return False
        
        return dfs(0)
            
