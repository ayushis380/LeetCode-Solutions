class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 
    
    # after the sum check we make sure there is a possible solution
    # an index might not be able to cover the cost if tank < 0 
    # but there will be an index present which will balance this negative value of tank
    # as sum(gas) >= sum(cost)
        tank, start = 0, 0 

        for i in range(len(gas)):
            tank += gas[i] - cost[i] # updating the car tank's value
            
            if tank < 0:
                tank = 0
                start = i + 1 # the index which kept tank +ve till the end
        
        return start