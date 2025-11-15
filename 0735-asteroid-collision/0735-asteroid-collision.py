class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0 and ast != 0:
                diff = stack[-1] + ast

                if diff == 0:
                    stack.pop()
                    ast = 0
                elif diff < 0: # add ast
                    stack.pop()
                else:
                    ast = 0 # not add ast, as its -ve
            
            if ast != 0:
                stack.append(ast)
        
        return stack