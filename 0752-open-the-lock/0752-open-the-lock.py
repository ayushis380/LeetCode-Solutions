class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
    # when we start from 0000, next we have 8 combinations at level 1 
    # as at each position we can go to next or last number in the wheel
    # shortest path using BFS 

        if "0000" in deadends or target in deadends:
            return -1
        
        queue = deque([("0000", 0)]) # state and turns
        visited = set(deadends) # we dont want to visit the dead ends, keep updating this

        def children(lock):
            result = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10) # 9 + 1 = 10 % 10 = 0
                result.append(lock[:i] + digit + lock[i+1:]) # include new digit, exclude old value

                digit = str((int(lock[i]) - 1 + 10) % 10) # 0 - 1 = -1 + 10 = 9 % 10 = 9
                result.append(lock[:i] + digit + lock[i+1:])

            return result
        
        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns

            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    queue.append((child, turns + 1)) # next level
        
        return -1