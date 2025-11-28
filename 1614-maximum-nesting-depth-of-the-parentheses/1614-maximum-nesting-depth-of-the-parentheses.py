class Solution:
    def maxDepth(self, s: str) -> int:
        maxd = 0
        balance = 0

        for ch in s:
            if ch == "(":
                balance += 1
            
            if ch == ")":
                balance -= 1
            
            maxd = max(maxd, balance)
        
        return maxd