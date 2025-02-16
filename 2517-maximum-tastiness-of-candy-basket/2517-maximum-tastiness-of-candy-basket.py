class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort() # pick candies in increasing order, making it easier to enforce a minimum difference.
        length = len(price)
        low, high = 0, price[-1] - price[0] # possible values for the tastiness range

        def isValid(mid):
            """Checks if we can select k candies with min difference >= mid."""
            count, last = 1, price[0] # Pick the first candy

            for i in range(1, length):
                if price[i] - last >= mid: # >= mid, then only mid can be smallest absolute difference
                    count += 1
                    last = price[i]
                    if count == k:
                        return True
            
            return False

        # Binary Search
        while low < high:
            # mid = low + (high - low) // 2  # Traditional binary search midpoint - rounds down the middle value, which can cause the search to terminate with a suboptimal mid

            mid = (low + high + 1) // 2  # +1 ensures that we are biasing the midpoint upwards, biases the midpoint upwards, Try a higher tastiness value as we need maximum tastiness
            if isValid(mid):
                low = mid  # Increase min difference
            else:
                high = mid - 1 # Reduce min difference
        
        return low