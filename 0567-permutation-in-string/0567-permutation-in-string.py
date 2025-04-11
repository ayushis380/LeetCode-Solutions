class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1, lens2 = len(s1), len(s2)
        if lens1 > lens2:
            return False
        
        fs1, fs2 = [0] * 26, [0] * 26
        
        # to maintain window size of len(s1)
        for i in range(lens1):
            fs1[ ord(s1[i]) - ord('a') ] += 1
            fs2[ ord(s2[i]) - ord('a') ] += 1
        
        for i in range(lens1, lens2):
            if self.helper(fs1, fs2): # check if all values match
                return True
            
            # to maintain window size of len(s1) - increase freq of end char - new addition
            # decrease window - decrease freq of start char 
            ch_end = ord(s2[i]) - ord('a')
            ch_start = ord(s2[i - lens1]) - ord('a')

            fs2[ch_end] += 1
            fs2[ch_start] -= 1

        return self.helper(fs1, fs2) # last window of len(s1)
    
    def helper(self, fs1, fs2):
        count = 0

        for i in range(26):
            if fs1[i] == fs2[i]:
                count += 1
        
        return True if count == 26 else False
        
        