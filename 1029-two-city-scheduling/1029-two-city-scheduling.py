class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        delta = []
        total = 0

        for i, cst in enumerate(costs):
            acost, bcost = cst
            delta.append([acost - bcost, i])
        
        delta.sort()
        low, high = 0, len(delta) -1

        while low < high:
            l, h = delta[low][1], delta[high][1]
            acost, bcost = costs[l][0], costs[h][1]
            total += acost + bcost

            low += 1
            high -= 1
        
        return total
        