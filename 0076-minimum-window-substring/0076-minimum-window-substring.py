class Solution:
    def minWindow(self, s: str, t: str) -> str:
        indices, minlen = [-1,-1], float("inf")
        start = 0 
        t_count = Counter(t)
        s_count = Counter()
        need = len(t_count)
        have = 0

        for i in range(len(s)):
            ch = s[i]
            s_count[ch] += 1

            if ch in t_count and s_count[ch] == t_count[ch]:
                have += 1
            
            while have == need:
                if (i - start + 1 < minlen):
                    minlen = i - start + 1
                    indices = [start, i]
                
                s_count[s[start]] -= 1
                if s[start] in t_count and s_count[s[start]] < t_count[s[start]]:
                    have -= 1
                
                start += 1
        
        l, r = indices
        return s[l : r+1 ] if minlen != float("inf") else ""

