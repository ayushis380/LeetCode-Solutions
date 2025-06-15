class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch) 
            else:
                substr = ""
                while stack[-1] != "[": # to get the characters inside []
                    substr = stack.pop() + substr # see the order its popped, original order to be maintained
                stack.pop() # pop "["

                k = ""
                while stack and stack[-1].isdigit(): # get the k value, a digit 
                    k = stack.pop() + k # form the k value
                stack.append(int(k) * substr) # append to stack k times the substr
        
        return "".join(stack)