class Solution:
    def validPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1

        def check(l, h):
            while l < h:
                if s[l] != s[h]:
                    return False
                
                l += 1
                h -= 1
            
            return True
        
        while low < high:
            if s[low] != s[high]:
                return check(low +1, high) or check(low, high -1)
            
            low += 1
            high -= 1
        
        return True