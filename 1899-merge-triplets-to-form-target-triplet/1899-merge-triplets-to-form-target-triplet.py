class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        check = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for ind in range(len(t)):
                if t[ind] == target[ind]:
                    check.add(ind)
        
        return True if len(check) == 3 else False