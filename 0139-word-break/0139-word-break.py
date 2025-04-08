class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length + 1)
        dp[length] = True

        for i in range(length - 1, -1, -1):
            for wrd in wordDict:
                if i + len(wrd) <= length and s[i: i+len(wrd)] == wrd:
                    print(wrd)
                    dp[i] = dp[i+len(wrd)]
        
        # if once set to True then break as the other values in wordDict can set this dp value to False
        # if found a True at ith index that means there is a possible way to form the string 
        # break to move to last index of string s
                if dp[i]: 
                    break
        print(dp)
        return dp[0]
