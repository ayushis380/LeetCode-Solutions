class Solution:
    def isPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1 # high started from len(s) - 1 as we will be checking s[high] value in the while loop

        while low < high:
            while low < high and not s[low].isalnum():
                low += 1
            
            while low < high and not s[high].isalnum():
                high -= 1
            
            if s[low].lower() != s[high].lower():
                return False
            
            low += 1
            high -= 1
        
        return True