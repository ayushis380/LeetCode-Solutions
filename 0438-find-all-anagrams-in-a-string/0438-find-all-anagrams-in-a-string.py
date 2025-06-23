class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        # window of len(p)
        pct, sct = defaultdict(int), defaultdict(int)
        for i in range(len(p)):
            pct[p[i]] += 1
            sct[s[i]] += 1
        
        # if match in first window
        res = [0] if pct == sct else []
        start = 0

        for end in range(len(p), len(s)):
            sct[s[end]] += 1
            sct[s[start]] -= 1

            if sct[s[start]] == 0:
                del sct[s[start]] 
            start += 1 # adjust new window and check if they match
            if sct == pct:
                res.append(start)
        
        return res