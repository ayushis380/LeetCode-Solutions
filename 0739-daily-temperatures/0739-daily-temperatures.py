class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                i_old, t_old = stack.pop()
                warmer[i_old] = i - i_old

            stack.append((i, t))
        
        return warmer