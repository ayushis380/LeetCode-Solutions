class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 0, 1

        for i in range(n):
            temp = two
            two = one + two
            one = temp
        
        return two