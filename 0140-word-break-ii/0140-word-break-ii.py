class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # O(n⋅2 ^n) = explore all paths, and forming string takes O(n)
        # SC 2 ^n
        wordSet = set(wordDict)
        n = len(s)
        result = []

        def backtrack(start, path):
            if start == n:
                result.append(" ".join(path))
                return
            
            for end in range(start + 1, n + 1): # n + 1 is important as we need end = n to exist
                word = s[start:end] 
                
                if word in wordSet:
                    path.append(word)
                    backtrack(end, path) # end becomes new start
                    path.pop()
        
        backtrack(0, [])
        return result