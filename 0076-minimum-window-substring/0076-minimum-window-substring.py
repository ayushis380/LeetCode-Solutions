class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_ct = Counter()
        t_ct = Counter(t)
        start = 0
        have, need = 0, len(t_ct)
        minlen = float("inf")
        l, r = -1, -1

        for i, ch in enumerate(s):
            s_ct[ch] += 1
            if ch in t_ct and s_ct[ch] == t_ct[ch]:
                have += 1
            
            while have == need:
                length = i - start + 1
                if minlen > length:
                    minlen = length
                    l, r = start, i
                
                ch_start = s[start]
                s_ct[ch_start] -= 1
                if ch_start in t_ct and s_ct[ch_start] < t_ct[ch_start]:
                    have -= 1
                
                start += 1
        
        return s[l: r+1]