class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dial = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        combinations = []
        def backtrack(path, level):
            if level == len(digits): # level = always 1 less than length, return when equal
                combinations.append(path)
                return 
            for ch in dial[digits[level]]:
                backtrack(path + ch, level +1)

        if digits:
            backtrack("", 0)
        return combinations