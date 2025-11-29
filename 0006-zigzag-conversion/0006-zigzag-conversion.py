class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # pattern between the distances between characters in each row
        if numRows == 1:
            return s
        
        result = ""
        increment = 2 * (numRows - 1)
        
        for r in range(numRows):
            for i in range(r, len(s), increment):
                result += s[i]

                if r > 0 and r < numRows -1 and (i + increment - 2 * r) < len(s):
                    result += s[i + increment - 2 * r] # in middle rows, number of characters increase - part of same section
        
        return result
            