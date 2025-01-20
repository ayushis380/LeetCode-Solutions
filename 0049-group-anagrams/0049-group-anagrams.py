class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)

        for s in strs:
            sort_s = "".join(sorted(s))
            anag[sort_s].append(s)
        
        return list(anag.values())
