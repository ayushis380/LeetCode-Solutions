class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        queue = deque()
        indegree = [0] * (n +1)
        dp = [0] * (n+1)

        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1
        
        for i in range(1, n+1):
            if indegree[i] == 0:
                queue.append(i)
                dp[i] = time[i-1]

        
        while queue:
            crs = queue.popleft()
            for nei in adj[crs]:
                dp[nei] = max(dp[nei], dp[crs] + time[nei-1])
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)
        print(dp)
        return max(dp)