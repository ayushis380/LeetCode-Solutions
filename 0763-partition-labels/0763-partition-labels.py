class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastind = {}
        size, end = 0, 0
        result = []

        for ind, ch in enumerate(s):
            lastind[ch] = ind
        
        for ind, ch in enumerate(s):
            size += 1
            end = max(end, lastind[ch])

            if end == ind:
                result.append(size)
                size = 0 
        
        return result