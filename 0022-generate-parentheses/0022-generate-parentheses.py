class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pairs = []
        p = []
        check = []
    
        def dfs(open, close):
            if open == close == n:
                pairs.append("".join(p))
                check.append(p.copy())
                return
            
            if open < n:
                p.append('(')
                dfs(open + 1, close)
                p.pop()
            
            if close < open:
                p.append(')')
                dfs(open, close + 1)
                p.pop()
        
        dfs(0, 0)
        print(check)
        return pairs