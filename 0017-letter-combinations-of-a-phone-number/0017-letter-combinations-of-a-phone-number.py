class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        output, path = [], []

        def dfs(i):
            if i >= len(digits):
                output.append("".join(path.copy()))
                return
            
            digit = digits[i]
            dial = phone[digit]
            for s in dial:
                path.append(s)
                dfs(i+1)
                path.pop()
        
        dfs(0)
        return output
        