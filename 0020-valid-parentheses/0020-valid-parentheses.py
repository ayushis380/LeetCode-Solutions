class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { 
            '}': '{', ')': '(', ']' : '[' 
        }
        stack = []

        for ch in s:
            if ch in closeToOpen:
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return False if len(stack) else True