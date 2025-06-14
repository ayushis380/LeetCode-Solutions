class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # n nodes and n-1 edges : undirected acyclic graph
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Bob simulation, DFS, he is moving towards root - only one path choice
# DFS is a natural choice because it fully explores each path before backtracking, allowing us to efficiently find the path Bob follows to the root.
        bobTime = defaultdict(int) # node on root path -> timestamp he visited

        def dfs(src, prev, ts):
            if src == 0:
                bobTime[src] = ts
                return True
            
            for nei in adj[src]:
                if nei == prev:
                    continue # avoid cycle, shouldnt go where we came from
                if dfs(nei, src, ts+1): # only becomes True when it gets True from the root 0
                    bobTime[src] = ts
                    return True
            
            return False
            
        dfs(bob, -1, 0)

        # Alice simulation, will always have amount of root node as bob != 0
        # discovers a lot of paths and picks maximum 
        # BFS systematically explores all nodes level by level, making it ideal for finding optimal paths
        q = deque([(0, 0, -1, amount[0])]) # node, time, parent, total profit
        res = float("-inf")

        while q:
            node, time, parent, profit = q.popleft()

            for nei in adj[node]:
                if nei == parent: # avoid cycle
                    continue

                nei_profit = amount[nei]
                nei_time = time + 1 # nei time, all neis of node will be visited at time + 1 as only one path is considered 

                if nei in bobTime:
                    if nei_time > bobTime[nei]: # if bob has reached the node before alice
                        nei_profit = 0
                    elif nei_time == bobTime[nei]: # if eqaul then divide it
                        nei_profit = nei_profit // 2 # if negative then also fine as amount is always even
                
                q.append((nei, nei_time, node, profit + nei_profit)) # keep building profit from the neighbors

            # this len check is added under nei for loop as if moved outside then it would take root's amount if it also had a len of 1 - so take only its neigbors and their neigbors
                if len(adj[nei]) == 1: # this is the leaf node - so one of the possible paths
                    res = max(res, profit + nei_profit)
        
        return res