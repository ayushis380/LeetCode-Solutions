class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = defaultdict(int)

        for ch in s:
            freq[ch] += 1
        
        for ch in t:
            freq[ch] -= 1
        
        for ch, val in freq.items():
            if val != 0:
                return False
        
        return True