class Solution:
    def minSteps(self, s: str, t: str) -> int:
# only need to focus on the positive value which implies that there are more instances of this character in t
# the two values (the sum of the positive and negative differences) are equal in absolute value! 
# The positive value comes from the character in t that needs to be replaced, the negative value comes from the character in s that waits for the corresponding replacement in t

        count = [0] * 26
        swaps = 0

        for i in range(len(s)):
            count[ord(t[i]) - ord('a')] += 1
            count[ord(s[i]) - ord('a')] -= 1
        
        for i in range(26):
            swaps += max(0, count[i]) # sum only the negative differences or only the positive differences
        
        return swaps
            