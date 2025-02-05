class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using a hash map instead of fixed size list
        # better when unicode chars are more 
        if len(s) != len(t):
            return False

        freq = defaultdict(int)

        for i in range(len(s)):
            freq[s[i]] += 1
            freq[t[i]] -= 1
        
        for val in freq.values():
            if val != 0:
                return False
        
        return True
