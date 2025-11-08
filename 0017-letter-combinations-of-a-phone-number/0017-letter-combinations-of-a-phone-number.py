class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        path = []
        result = []

        def dfs(i):
            if i >= len(digits):
                result.append("".join(path))
                return
            
            dgt = digits[i]
            letters = pad[dgt]
            
            for ch in letters:
                path.append(ch)
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return result