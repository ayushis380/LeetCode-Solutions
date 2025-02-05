class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(NKlogK) as we are sorting strings here
        # K is the maximum length of a string
        
        group = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s)) # sorted doesnt modify the string
            group[key].append(s)
        
        return list(group.values())