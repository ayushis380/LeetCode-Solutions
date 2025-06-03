class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1

        while low < high:
            while low < high and not s[low].isalnum(): # low <= high condition shouldnt come as it will make low and high out of bounds
                low += 1
            
            while low < high and not s[high].isalnum():
                high -= 1
            
            print(low)
            if s[low].lower() != s[high].lower():
                return False
        
            low += 1
            high -=1
        
        return True
