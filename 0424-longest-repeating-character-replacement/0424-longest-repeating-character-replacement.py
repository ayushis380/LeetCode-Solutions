class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxfreq = 0
        maxlen = 0
        start = 0

        for end in range(len(s)):
            count[s[end]] += 1
            maxfreq = max(maxfreq, count[s[end]])
            if (end - start + 1) - maxfreq > k:
                count[s[start]] -= 1
                start += 1
            
            maxlen = max(maxlen, end - start + 1)
        
        return maxlen