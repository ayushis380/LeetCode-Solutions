class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    # DFS Top Down
        m, n = len(word1), len(word2)
        dp = {}

        def dfs(i, j):
    # end of word1, last row where word1 is empty, so we need n - j operations
    # at each cell, dp[(i,j)]: think of i and j taking all chars after it including itself
    # as we start filling the table from last cell and in reverse
            if i == m: 
                return n - j
    # end of word2, last col where word2 is empty then we need m - i operations
            if j == n:
                return m - i
            
            if (i,j) in dp:
                return dp[(i, j)] # memoiz
            
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
    # we insert a char to match with word2, so word2 moves but word1 doesnt as inserted char is before i
    # so char at i still needs to be considered
                insert_op = dfs(i, j+1)
    
    # when deleted from word1 then move to next char but char in word2 doesn't match yet
                delete_op = dfs(i+1, j)
    
    # when replace that means word1 char at i is replaced with something that word2 has at j 
    # so both indexes can increase
                replace_op = dfs(i + 1, j+1)
    
    # one added op when we take either of 3 
                dp[(i, j)] = 1 + min(insert_op, delete_op, replace_op)

            return dp[(i, j)]
        
        return dfs(0, 0)