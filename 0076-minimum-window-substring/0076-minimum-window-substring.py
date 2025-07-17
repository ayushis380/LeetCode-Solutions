class Solution:
    def minWindow(self, s: str, t: str) -> str:

        indices, minw = [-1, -1], float("inf")
        window, countT = {}, {} # window is to count freq in valid window 
        start = 0

        # get unique chars from t, which we need
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        # once have == need, shrink window to look for smaller window
        have, need = 0, len(countT)

        for end in range(len(s)):
            ch = s[end]
            window[ch] = window.get(ch, 0) + 1 

            if ch in countT and window[ch] == countT[ch]:
                have += 1 # match
            
            while have == need:
                if (end - start + 1) < minw: # update window if small one found
                    indices = [start, end]
                    minw = end - start + 1
                
                window[s[start]] -= 1 # shrink window
                # check if window is still valid, otherwise have should be reduced
                # window[character] >= countT[character] if this is true then have cond is fulfilled
                # window has atleast those characters required by string t
                # more freq means duplication in string s 
                if s[start] in countT and window[s[start]] < countT[s[start]]:
                    have -= 1
                start += 1
        
        l, r = indices
        return s[l: r+1] if minw != float("inf") else ""


