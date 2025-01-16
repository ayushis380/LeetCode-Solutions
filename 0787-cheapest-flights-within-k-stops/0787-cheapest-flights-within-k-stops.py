class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford Algo
        prices = [float("inf")] * n
        prices[src] = 0 # start checking from here

        for i in range(k+1): # think k = 0, then you can only reach to src neighbors
            temp_prices = prices.copy()

            for start, dest, cost in flights:
                if prices[start] == float("inf"): # this start point is not reachable yet
                    continue
            # update and compare with temp_prices as its a for loop, and prices wont have updated values
            # it will be updated after the for loop
                if prices[start] + cost < temp_prices[dest]: # compare with existing price of destination
                    temp_prices[dest] = prices[start] + cost
            
            prices = temp_prices
        
        return -1 if prices[dst] == float("inf") else prices[dst]
