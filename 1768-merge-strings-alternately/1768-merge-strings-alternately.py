class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        p1, p2, ind = 0, 0, 0
        merged = ""

        while p1 < m and p2 < n:
            if not ind % 2:
                merged += word1[p1]
                p1 += 1
            else:
                merged += word2[p2]
                p2 += 1
            
            ind += 1
        
        if p1 < m:
            merged += word1[p1:m]
        
        if p2 < n:
            merged += word2[p2:n]
        
        return merged



