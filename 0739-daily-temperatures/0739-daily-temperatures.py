class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        # monoton decreasing stack
        for i, tem in enumerate(temperatures):
            while stack and stack[-1][1] <= tem:
                i_pop, tem_pop = stack.pop()
                result[i_pop] = i - i_pop
            
            stack.append((i, tem))

        return result