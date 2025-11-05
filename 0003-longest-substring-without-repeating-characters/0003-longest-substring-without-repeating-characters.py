class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        start = 0
        maxlen = 0

        for end, ch in enumerate(s):
            while ch in unique:
                unique.remove(s[start])
                start += 1
            
            maxlen = max(maxlen, end - start + 1)
            unique.add(ch)
        
        return maxlen
