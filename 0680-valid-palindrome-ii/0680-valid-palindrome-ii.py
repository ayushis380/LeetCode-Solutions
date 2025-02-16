class Solution:
    def validPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1

        def is_Palindrome(low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            
            return True
        
        while low < high:
            if s[low] != s[high]:
                return is_Palindrome(low + 1, high) or is_Palindrome(low, high - 1)
            
            low += 1
            high -= 1
        
        return True