class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0

            half = power(x, n//2)
            res = half * half

            if n % 2:
                res *= x
            return res
        
        value = power(x, abs(n))
        if n >= 0:
            return value
        else:
            return 1/value
