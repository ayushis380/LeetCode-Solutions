class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        indexes = set() # to store ind of matching target

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue # remove bad triplets which are greater than target
            
            # now remaining ones should be checked
            for key, value in enumerate(t):
                if value == target[key]:
                    indexes.add(key)
        
        return True if len(indexes) == 3 else False
            
