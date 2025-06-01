class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        low, high = 2, x//2

        while low <= high:
            mid = low + (high - low)//2
            val = mid * mid

            if val == x:
                return mid
            elif val < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return high
        #   After the loop when low > high, then high is the largest integer such that high^2 ≤ x.
        # This is the floor of the square root.




