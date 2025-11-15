class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = min([len(s) for s in strs])
        if minlen == 0:
            return ""
        
        result = ""
        for i in range(minlen):
            ch = strs[0][i]
            for j in range(len(strs)):
                if ch != strs[j][i]:
                    return result
            
            result += ch
        
        return result
                