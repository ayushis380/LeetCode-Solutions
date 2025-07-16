class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])

        while True:
            val = 0
            while n > 0:
                quo, rem = divmod(n, 10)
                val += rem ** 2
                n = quo
            
            if val == 1:
                return True
            elif val in seen:
                return False
            
            seen.add(val)
            n = val
        
        return False
