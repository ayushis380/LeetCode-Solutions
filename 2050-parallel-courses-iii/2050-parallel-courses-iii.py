class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        max_times = {} # dp to check for already visited courses, course -> max time it took to complete
        adj = defaultdict(list)

        for pr, nxt in relations:
            adj[pr].append(nxt)

        def dfs(src):
            if src in max_times:
                return max_times[src]
            
            res = time[src - 1] # own time
            for nei in adj[src]:
                res = max(res, time[src - 1] + dfs(nei)) # max from all nei of src
            
            max_times[src] = res
            return res
        
        for i in range(1, n + 1):
            dfs(i)

        return max(max_times.values()) # critical path which takes max time to complete
        
