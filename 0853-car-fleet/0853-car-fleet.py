class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(p, s) for p, s in zip(position, speed)]
        time.sort(reverse=True) # sorted on basis of position in reverse

        stack = []

        for p, s in time:
        # car cannot pass another car so cars in middle can have different speeds 
        # so it is sorted as per positions from last
            stack.append((target - p)/s) # positions closer to target are added first 

        # ind = -1 has the newly added value, ind = -2 the old value
        # if new value is less than old value it means car at -1 is faster than -2 and it will catch up
        # as cars can't go ahead if they are faster, new value is popped
        # car will move at the speed of old value

            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()
        
        return len(stack) # stack has all the fleet speeds (slower speeds as faster cars catch up to slower ones)

