class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # below code doesnt consider if we start from 1st index
        # length = len(cost)

        # for i in range(2, length):
        #     cost[i] += min(cost[i-1], cost[i-2])
        
        # return cost[length-1]

        # we can either start from 0th or 1st index
        length = len(cost)

        for i in range(2, length):
            cost[i] += min(cost[i-1], cost[i-2])
        
        return min(cost[length-1], cost[length-2])