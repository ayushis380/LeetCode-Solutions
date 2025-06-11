class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                diff = stack[-1] + ast

                if diff > 0:
                    ast = 0
                elif diff < 0:
                    stack.pop()
    # not required below as we keep the original ast value when diff < 0, this ast is < 0 will be compared to pending values of the stack
                    # ast = diff 
                else:
                    stack.pop()
                    ast = 0
            
            if ast:
                stack.append(ast)
        
        return stack