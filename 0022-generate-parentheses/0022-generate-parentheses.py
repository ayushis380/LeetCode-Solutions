class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        current = []
        combinations = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                combinations.append("".join(current))
                return
            
            if openN < n:
                current.append('(')
                backtrack(openN +1, closeN)
                current.pop()
            
            if closeN < openN:
                current.append(')')
                backtrack(openN, closeN + 1)
                current.pop()
        
        backtrack(0,0)
        return combinations