class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        minlen = min([len(s) for s in strs])

        if minlen == 0:
            return ""
        
        for i in range(minlen):
            ch = strs[0][i]

            for s in strs:
                if ch != s[i]:
                    return common
            
            common += ch
        
        return common