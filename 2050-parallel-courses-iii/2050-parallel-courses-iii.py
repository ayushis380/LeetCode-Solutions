class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        dp = {}
        adj = defaultdict(list)

        for u, v in relations:
            adj[u].append(v)

        def dfs(src):
            if src in dp:
                return dp[src]
            
            res = time[src-1] # makes sure we take course's own month as some wont have neighbors
            for nei in adj[src]:
                res = max(res, time[src-1] + dfs(nei))
            
            dp[src] = res
            return res
        
        for i in range(1, n+1):
            dfs(i)

        # print(dp)
        return max(dp.values())
