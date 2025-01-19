class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy approach O(n)
        length = len(nums)
        steps = 0
        left, right = 0, 0
    
    # checking till right reaches the end
    # task is to reach the end and if right is at end we can return the steps
        while right < length - 1:
            farthest = 0 # at every index check what farthest index can be reached
    # starts at left = right = 0 
    # in every execution we get a set of indexes that can be reached (like bfs, at each level we have these set of indexes)
    # 2 1 3 -> this means from index = 0 we can go to either index = 1 or index = 2
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
    
    # values for next iteration, picking the next indexes
            left = right + 1  # at each level indexes range from left to right
            right = farthest # in next iter, it will look for indexes reachable from farthest
            steps += 1 # each iter will take us closer to the last index
        
        return steps
