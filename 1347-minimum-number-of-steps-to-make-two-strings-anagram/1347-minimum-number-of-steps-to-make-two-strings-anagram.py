class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = [0] * 26
        swaps = 0

        for i in range(len(s)):
            count[ord(t[i]) - ord('a')] += 1
            count[ord(s[i]) - ord('a')] -= 1
        
        for i in range(26):
            swaps += max(0, count[i]) # sum only the negative differences or only the positive differences
        
        return swaps
            