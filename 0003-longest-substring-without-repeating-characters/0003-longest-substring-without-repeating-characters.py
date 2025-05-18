class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        start = 0
        maxlen = 0

        for end in range(len(s)):
            
            while s[end] in unique:
                unique.remove(s[start])
                start += 1
            
            maxlen = max(maxlen, end - start + 1)
            unique.add(s[end])
        
        return maxlen