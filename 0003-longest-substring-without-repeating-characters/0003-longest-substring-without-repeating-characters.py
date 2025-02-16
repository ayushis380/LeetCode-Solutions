class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        maxlen, start = 0, 0

        for end in range(len(s)):
            while s[end] in unique:
                unique.remove(s[start])
                start += 1
            
            unique.add(s[end])
            maxlen = max(maxlen, end - start + 1)
        
        return maxlen