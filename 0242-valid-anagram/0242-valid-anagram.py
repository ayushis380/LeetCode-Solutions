class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = defaultdict(int)

        for i in range(len(s)):
            ch_s = s[i]
            ch_t = t[i]

            count[ch_s] += 1
            count[ch_t] -= 1
        
        for i in range(len(s)):
            if count[s[i]] != 0:
                return False
        
        return True