class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:
            while stack and stack[-1] > n and k:
                stack.pop() # keep monotonically increasing
                k -= 1
            
            stack.append(n)
        
        stack = stack[: len(stack) - k] # remove last k chars as those will make a bigger number

        i = 0
        while i < len(stack) and stack[i] == "0":
            i += 1
        
        stack = stack[i:]
        return "".join(stack) if stack else "0"