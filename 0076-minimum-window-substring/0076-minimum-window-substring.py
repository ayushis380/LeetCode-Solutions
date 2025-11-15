class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        s_map = Counter()
        t_map = Counter(t)
        need, have = len(t_map), 0
        start = 0
        left, right = 0, 0
        minlen = float("inf")

        for i, ch in enumerate(s):
            s_map[ch] += 1
            if ch in t_map and t_map[ch] == s_map[ch]:
                have += 1
            
            while need == have:
                if minlen > i - start + 1:
                    minlen = i - start + 1
                    left, right = start, i + 1
                
                ch_st = s[start]
                s_map[ch_st] -= 1
                if ch_st in t_map and s_map[ch_st] < t_map[ch_st]:
                    have -= 1
                
                start += 1
        
        return s[left: right]
