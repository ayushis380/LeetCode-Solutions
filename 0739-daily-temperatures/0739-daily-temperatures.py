class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, tmp in enumerate(temperatures):
            
            while stack and stack[-1][0] < tmp:
                old_tmp, old_ind = stack.pop()
                result[old_ind] = i - old_ind
            
            stack.append((tmp, i))
        
        return result