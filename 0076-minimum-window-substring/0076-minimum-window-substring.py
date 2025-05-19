class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_cnt = Counter(t)
        s_cnt = Counter()
        need, have = len(t_cnt), 0
        start = 0
        minlen = float("inf")
        left, right = -1, -1

        for end, ch in enumerate(s):
            s_cnt[ch] += 1

            if ch in t_cnt and t_cnt[ch] == s_cnt[ch]:
                have += 1
            
            while have == need:
                length = end - start + 1
                
                if minlen > length:
                    minlen = length
                    left, right = start, end + 1
                
                ch_start = s[start]
                s_cnt[ch_start] -= 1 # look for smaller window and see if count condition is still satisfied

                if ch_start in t_cnt and s_cnt[ch_start] < t_cnt[ch_start]:
                    have -= 1 # condition need to have >= : means freq of a character in s can be greater than freq of that same character in t but not less 
                
                start += 1 # keep decreasing the window - until have != need
        
        return s[left: right]

            


