class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0] # x < 0 evaluates to True → which is 1 in Python → so it picks -1 from the list
        rev, x = 0, abs(x)

        while x:
            x, mod = divmod(x, 10) # (x // 10, x % 10)
            rev = rev * 10 + mod

            if rev > 2**31 - 1: # -2,147,483,648 to 2,147,483,647
                return 0
        
        return sign * rev