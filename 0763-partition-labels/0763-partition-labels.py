class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastInd = {}
        result = []
        for i, ch in enumerate(s):
            lastInd[ch] = i
        
        size = 0
        end = 0
        for i in range(len(s)):
            end = max(end, lastInd[s[i]])
            if end > i:
                size += 1
            else:
                result.append(size+1)
                size = 0
                end = 0

        return result