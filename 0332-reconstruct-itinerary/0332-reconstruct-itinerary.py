class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's Algorithm (Iteration)
        # O(E log E) and O(E)
        adj = defaultdict(list)

        for start, end in sorted(tickets)[::-1]: # add in reverse of sorted tickets, so that when list is popped the lower lexigraphical value is taken
            adj[start].append(end)
        
        stack = ["JFK"]
        iti = []

        while stack:
            curr = stack[-1]
            if not adj[curr]: # when no flights left for adj[curr] then add to result, can be a dead end or when all are visited
                iti.append(stack.pop())
            else:
                stack.append(adj[curr].pop()) # keep adding 
        
        return iti[::-1] # reverse 