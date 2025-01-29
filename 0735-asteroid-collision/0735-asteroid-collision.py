class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # when top of stack is +ve and ast is -ve then only we have a different direction
            while stack and stack[-1] > 0 and a < 0:
                diff = stack[-1] + a # this flag to find what action to take
                
                if diff < 0:
                    stack.pop() # a wins so remove +ve value from stack
                elif diff > 0:
                    a = 0 # bigger value wins, to stop while as ast value can never be 0
                else:
                    a = 0
                    stack.pop() # both make them 0
            
            if a:
                stack.append(a) # if a is not 0 then add

        return stack
            
        