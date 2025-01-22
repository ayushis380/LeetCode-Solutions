class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxlen = 0
        self.maxpalin = ""

        for i in range(len(s)):
            self.palindrome(i, i, s)
            self.palindrome(i, i+1, s)
        
        return self.maxpalin
    
    def palindrome(self, left, right, s):
        result = ""
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            curlen = right - left + 1
            
            if curlen > self.maxlen:
                self.maxlen = curlen
                result = s[left:right + 1]
            
            left -= 1
            right += 1
        
        if len(result) == self.maxlen:
            self.maxpalin = result
    
