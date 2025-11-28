class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        diff = []
        total = 0

        for i, cst in enumerate(costs):
            acost, bcost = cst
            diff.append([acost - bcost, i])
        
        diff.sort(key= lambda x: x[0])
        print(diff)
        i, j = 0, len(diff) - 1

        while i < n:
            indA, indB = diff[i][1], diff[j][1]
            acost, bcost = costs[indA][0], costs[indB][1]
            total += acost + bcost

            i += 1
            j -= 1
        
        return total
        