class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        minlen = min([len(s) for s in strs])

        if minlen == 0:
            return ""

        for i in range(minlen):
            char = strs[0][i] # first string in strs

            for st in strs:
                if st[i] != char: # compare the char with all other strings for that index
                    return common
            
            common += char
        
        return common