class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for s in strs:
            # key = sorted(s)
            key = "".join(sorted(s))
            store[key].append(s)
        
        return list(store.values())