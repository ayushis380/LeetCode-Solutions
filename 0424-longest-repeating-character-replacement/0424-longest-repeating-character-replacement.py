class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = {}
        start = 0
        maxfreq = 0 # once we have a max value we wont change it if we get a less freq char as it maximise res we need to maximize maxfreq, 
        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            maxfreq = max(maxfreq, freq[s[end]])
            while (end-start+1) - maxfreq > k:
                freq[s[start]] -= 1
                start +=1

            res = max(res, end-start+1)
        return res