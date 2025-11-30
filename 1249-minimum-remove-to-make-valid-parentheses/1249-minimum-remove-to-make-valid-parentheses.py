class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def check(s, openSym, closeSym):
            result = ""
            balance = 0
            
            for ch in s:
                if ch == openSym:
                    balance += 1
                elif ch == closeSym:
                    if balance == 0:
                        continue
                    balance -= 1
                result += ch
            
            return result
        
        s = check(s, "(", ")")
        s = check(s[::-1], ")", "(")
        
        # aa = "let(a)("
        # print(aa[::-1])
        return s[::-1]