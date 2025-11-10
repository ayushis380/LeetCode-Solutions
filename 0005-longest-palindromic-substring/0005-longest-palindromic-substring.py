class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.maxlen = 0
        self.result = ""

        for i in range(n):
            self.check(i, i, s)
            self.check(i, i + 1, s)
        
        return self.result
    
    def check(self, low, high, s):
        while low >= 0 and high < len(s):
            if s[low] != s[high]:
                break
            if (high - low + 1) > self.maxlen:
                self.maxlen = (high - low + 1)
                self.result = s[low:high+1]
            
            low -= 1
            high += 1
