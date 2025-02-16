class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        result, minlen = [], float("inf")
        s_count = defaultdict(int)
        t_count = Counter(t)
        need, have = len(t_count), 0
        start = 0

        for end in range(len(s)):
            ch = s[end]
            s_count[ch] += 1

            if ch in t_count and t_count[ch] == s_count[ch]:
                have += 1
            
            while have == need:
                length = end - start + 1
                
                if minlen > length:
                    minlen = length
                    result = s[start: end + 1]
                
                ch_start = s[start]
                s_count[ch_start] -= 1

                # only decrement when count of ch in s is less than the count in t
                # it makes the window invalid
                # if we have count greater than its fine
                if ch_start in t_count and s_count[ch_start] < t_count[ch_start]:
                    have -= 1
                
                start += 1
        
        return result if result != [] else ""
            
            
            

        