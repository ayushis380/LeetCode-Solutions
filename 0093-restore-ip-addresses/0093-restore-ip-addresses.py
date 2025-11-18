class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n > 12:
            return [] # cant be formed
        
        result = []

        def backtrack(i, dots, currIp):
            if dots == 4 and i == n: # reached end
                result.append(currIp[:-1]) # currIp last chat will be . so not add that
                return
            if dots > 4:
                return 
            
            for j in range(i, min(i+3, n)): # every number can be max 3 len
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"): # integer shoulnt start with 0
                    backtrack(j + 1, dots + 1, currIp + s[i:j+1] + ".")
        
        backtrack(0, 0, "")
        return result