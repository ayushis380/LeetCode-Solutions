class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window = len(s1)
        window_count = Counter()

        # maintain a window of size s1 
        for i in range(len(s2)):
            
            window_count[s2[i]] += 1
            start = i - window

            if i >= window:
                if window_count[s2[start]] == 1:
                    del window_count[s2[start]] # 1 -1 = 0 so delete 
                else:
                    window_count[s2[start]] -= 1 # otherwise decrease freq
            
            if s1_count == window_count:
                return True
        
        return False
