class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(NK) TC and SC, as we are counting for each 
        # K is the maximum length of a string
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1
            
            result[tuple(count)].append(s)
        
        return list(result.values())