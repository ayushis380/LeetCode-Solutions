class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = calculate(x, n//2)
            res = res * res

            if n % 2 == 1:
                return res * x
            
            return res
        
        res = calculate(x, abs(n))

        if n >=0:
            return res
        else:
            return 1/res