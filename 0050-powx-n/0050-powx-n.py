class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calc(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            half = calc(x, n//2)
            result = half * half
            
            if n % 2:
                result *= x
            return result

        res = calc(x, abs(n))
        if n >= 0:
            return res
        else:
            return 1/res