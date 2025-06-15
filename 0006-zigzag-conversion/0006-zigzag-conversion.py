class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        result = ""

        for r in range(numRows):
             increment = 2 * (numRows - 1) # to get the next character in same row

             for i in range(r, len(s), increment):
                result += s[i]

                # for middle rows, we have an extra character to be added - its like a V
                # i + increment - 2 * r = formula for it, it decreases as we go deep in V
                if (r > 0 and r < numRows - 1 and 
                    i + increment - 2 * r < len(s)):
                    result += s[i + increment - 2 * r]
        
        return result