class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_ct = Counter(s1)
        s2_ct = Counter()
        start = 0

        for end, ch in enumerate(s2):
            ch_start = s2[start]
            s2_ct[ch] += 1

            if end >= len(s1):
                s2_ct[ch_start] -= 1
                start += 1

                if s2_ct[ch_start] == 0:
                    del s2_ct[ch_start]
            
            if s1_ct == s2_ct:
                return True
            
        return False

