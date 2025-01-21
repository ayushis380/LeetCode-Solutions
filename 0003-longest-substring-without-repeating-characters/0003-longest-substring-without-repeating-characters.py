class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        start, result = 0, 0

        for end in range(len(s)):
            ch = s[end]
            count[ch] += 1

            while count[ch] > 1:
                ch_start = s[start]
                count[ch_start] -= 1
                start += 1
            
            result = max(result, end - start + 1)

        return result