class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            output[key].append(s)
        
        print(output.values())
        return list(output.values())