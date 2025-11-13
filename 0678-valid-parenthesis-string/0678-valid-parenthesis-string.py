class Solution:
    def checkValidString(self, s: str) -> bool:
# with rows representing different indices of the string s and columns representing different counts of opening brackets. Each cell stores a boolean value indicating whether the string from the current index with the given count of opening brackets is valid or not.
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def check(i, open_ct): # index, open_ct
            if i >= n:
                return open_ct == 0
            
            if dp[i][open_ct] != -1:
                return dp[i][open_ct] == 1
            
            result = False
            if s[i] == "*":
                result |= check(i + 1, open_ct + 1) # for '('
                if open_ct > 0: # for ')' need to be +ve
                    result |= check(i + 1, open_ct - 1) 
                result |= check(i + 1, open_ct) # empty string for *
            else:
                if s[i] == '(':
                    result |= check(i + 1, open_ct + 1)
                elif open_ct > 0: # for ')'
                    result |= check(i + 1, open_ct - 1)
            
            dp[i][open_ct] = 1 if result else 0 # able to reach a valid string for this (i, open_ct) pair
            return result

        return check(0, 0)