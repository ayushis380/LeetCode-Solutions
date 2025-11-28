class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0

        for ch in s:
            if ch != ']':
                stack.append(ch) # push all, to find nested strings
            else:
                word = ""
                while stack[-1] != '[':
                    word = stack.pop() + word
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit(): # k can be 23 - all in chars
                    k = stack.pop() + k
                
                stack.append(int(k) * word)
                
        return "".join(stack)

        