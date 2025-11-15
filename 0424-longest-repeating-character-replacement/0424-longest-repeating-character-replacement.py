class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        maxlen = 0
        count = defaultdict(int)

        for end, ch in enumerate(s):
            count[ch] += 1
            while (end - start + 1) - max(count.values()) > k:
                ch_start = s[start]
                count[ch_start] -= 1
                start += 1
            
            maxlen = max(maxlen, end - start + 1)
        
        return maxlen