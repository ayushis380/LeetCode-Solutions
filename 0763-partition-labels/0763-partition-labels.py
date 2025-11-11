class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastInd = {}
        result = []
        for i, ch in enumerate(s):
            lastInd[ch] = i
        
        size = 0
        end = 0
        for i in range(len(s)):
            size += 1
            end = max(end, lastInd[s[i]])
            if end == i: # when the max index of a sring is reached 
                result.append(size)
                size = 0

        return result