class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        n = len(s)

        for i in range(n):
            self.palindrome(i, i, s)
            self.palindrome(i, i + 1, s)
        
        return self.count
    
    def palindrome(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.count += 1
            l -= 1
            r += 1
        