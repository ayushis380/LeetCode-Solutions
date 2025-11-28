class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        low, high = 0, len(s) - 1
        front = ""
        back = ""

        while low <= high:
            while low < high and s[low].isalpha():
                front += s[low]
                low += 1

            while high >= 0 and s[high].isalpha():
                back += s[high]
                high -= 1
            
            if s[low] == "(" and s[high] == ")":
                front += "("
                back += ")"
                low += 1
                high -= 1
            elif s[low] == ")":
                low += 1
            elif s[high] == "(":
                high -= 1
        
        # print(front)
        # print(back)
        return front + back[::-1]
            