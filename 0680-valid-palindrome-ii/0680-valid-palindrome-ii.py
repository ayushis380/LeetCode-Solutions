class Solution:
    def validPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1
        flag = False

        def check(low, high):
            nonlocal flag
            if low > high:
                return True

            res = False
            if s[low] == s[high]:
                res = check(low + 1, high - 1)
            elif flag == True:
                return False
            elif flag == False:
                flag = True
                res = check(low + 1, high) or check(low, high - 1)
            
            return res
        
        return check(low, high)