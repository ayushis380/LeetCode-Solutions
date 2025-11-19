class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        stack = [0]

        while stack:
            node = stack.pop()
            for nei in rooms[node]:
                if nei not in visited:
                    stack.append(nei)
                    visited.add(nei)
        
        return True if len(visited) == len(rooms) else False
