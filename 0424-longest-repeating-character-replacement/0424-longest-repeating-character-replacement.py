class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        start = 0 
        maxlen = 0

        for end, ch in enumerate(s):
            count[ch] += 1
            length = end - start + 1 # can add k other chars, take max(count) so that least k is required
            if length - max(count.values()) > k:
                count[s[start]] -= 1
                start += 1
            
            maxlen = max(maxlen, end - start + 1)
        
        return maxlen