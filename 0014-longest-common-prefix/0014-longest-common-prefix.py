class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = min(len(s) for s in strs)

        if minlen == 0:
            return ""
        
        prefix = ""

        for i in range(minlen):
            common = strs[0][i]

            for s in strs:
                if s[i] != common:
                    return prefix
            
            prefix += common
        
        return prefix
