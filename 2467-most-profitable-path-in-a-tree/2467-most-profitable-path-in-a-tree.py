class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        bobtime = defaultdict(int)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, prev, ts):
            if node == 0:
                bobtime[node] = ts
                return True
            
            for nei in adj[node]:
                if nei == prev:
                    continue
                if dfs(nei, node, ts + 1):
                    bobtime[node] = ts
                    return True
            
            return False
        
        dfs(bob, -1, 0)

        queue = deque([(0, 0, amount[0], -1)]) # ts = 0, node = 0, amt = amount[0], prev = -1
        income = float("-inf")

        while queue:
            ts, node, profit, prev = queue.popleft()

            for nei in adj[node]:
                if nei == prev:
                    continue
                
                nei_profit = amount[nei]
                nei_time = ts + 1

                if nei in bobtime:
                    if nei_time > bobtime[nei]:
                        nei_profit = 0
                    elif nei_time == bobtime[nei]:
                        nei_profit = nei_profit//2
                
                queue.append((nei_time, nei, profit + nei_profit, node))

                if len(adj[nei]) == 1:
                    income = max(income, profit + nei_profit)
        
        return income
                
                

        
