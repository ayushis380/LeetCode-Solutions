class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        visited = set(deadends)
        queue = deque([("0000", 0)])

        def children(lock):
            result = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                result.append(lock[:i] + digit + lock[i+1:]) 

                digit = str((int(lock[i]) - 1 + 10) % 10)
                result.append(lock[:i] + digit + lock[i+1:]) 
            
            return result
        
        while queue:
            lock, turns = queue.popleft()

            if lock == target:
                return turns

            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    queue.append((child, turns + 1))
        
        return -1