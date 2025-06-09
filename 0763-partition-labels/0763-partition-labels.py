class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastind = {} # to store last index of a char
        res = []
        for i, c in enumerate(s):
            lastind[c] = i 
        size, end = 0, 0
        
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastind[c]) # only update if max for new char
            if end == i: # for atmost condition
                res.append(size)
                size = 0
        
        return res

        
