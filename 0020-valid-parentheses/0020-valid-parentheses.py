class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            '}' : '{', ')': '(', ']': '['
        }
        stack = []

        for ch in s:
            if ch in closeToOpen:
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()
                    continue
                else:
                    return False
            
            stack.append(ch)
        
        return False if len(stack) else True