class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # window of s1 len if present in s2
        count_s1 = Counter(s1)
        count_s2 = Counter()
        length = len(s1)
        start = 0

        for end, ch in enumerate(s2):
            count_s2[ch] += 1

            if end - start + 1 > length:
                count_s2[s2[start]] -= 1
                start += 1
            
            if count_s1 == count_s2:
                return True
        
        return False