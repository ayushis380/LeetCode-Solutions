class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == "+":
                stack.append(stack.pop() + stack.pop())
            elif ch == "-":
                fn = stack.pop()
                stack.append(stack.pop() - fn)
            elif ch == "*":
                stack.append(stack.pop() * stack.pop())
            elif ch == "/":
                fn = stack.pop()
                stack.append(int(stack.pop() / fn))
            else:
                stack.append(int(ch))
        
        return stack[-1]