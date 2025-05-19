class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(pos, sp) for pos, sp in zip(position, speed)]
        arr.sort(reverse=True)
        stack = []

        for p, s in arr:
            t = (target - p) / s

            stack.append(t)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack) 
