class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.palin = ""
        self.maxlen = 0

        for i in range((len(s))):
            self.helper(i, i, s)
            self.helper(i, i + 1, s)
        
        return self.palin
    
    def helper(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > self.maxlen:
                self.palin = s[l: r+1]
                self.maxlen = r - l + 1
            
            l -= 1
            r += 1
            
