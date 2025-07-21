class Solution:
    def totalNQueens(self, n: int) -> int:
        # O(N^2) to build each valid solution, the amount of valid solutions S(N) does not grow nearly as fast as N!
        # so O(N!+ S(N) * N ^2) = O(N!)
        cols = set()
        posDiag = set() # r + c
        negDiag = set() # r - c
        result = 0

        def backtrack(r):
            # print("row is ", r)
            nonlocal result 
            if r == n:
                result += 1
                return
            
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        
        backtrack(0)
        return result