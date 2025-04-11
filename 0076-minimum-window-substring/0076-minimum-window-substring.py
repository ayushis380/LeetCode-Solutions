class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        count_s = Counter()
        count_t = Counter(t)
        have, need = 0, len(count_t)
        start = 0
        l, r = -1, -1 
        minlen = float("inf")

        for end in range(len(s)):
            ch = s[end]
            count_s[ch] += 1

            if ch in count_t and count_t[ch] == count_s[ch]: # if count_s[ch] >= count_t[ch], have not increased as it would have already been increased when they were equal - have shoulld be updated per new character
                have += 1
            
            while have == need:
                length = end - start + 1
                
                if minlen > length:
                    minlen = length
                    l, r = start, end + 1

                ch_st = s[start]
                count_s[ch_st] -= 1 # have == need so decrease the window to look for a smaller window which satisfies this condition

                if ch_st in count_t and count_s[ch_st] < count_t[ch_st]:
                    have -= 1
                
                start += 1
        
        return s[l : r]
