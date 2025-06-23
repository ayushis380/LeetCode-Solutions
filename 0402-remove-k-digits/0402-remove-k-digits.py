class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [] # monotonic increasing 
        # egs 5 4 3 2 1 - its better to remove greater values to get a smaller value
        # 1 2 3 4 5 - better to remove 5, so here also greater value is removed
        # 9 1 9 9 - if first 9 is removed we get 1 9 9 and if last 9 is removed we get 9 1 9 - so better to remove lowest significant val

        for n in num:
            while stack and stack[-1] > n and k:
                stack.pop()
                k -= 1
            
            stack.append(n)
        
        stack = stack[: len(stack) - k] # last k chars can be ignored
        
        i = 0
        while i < len(stack) and stack[i] == '0': # remove all zeros
            i += 1

        stack = stack[i:]
        return ''.join(stack) if stack else '0'
        
        