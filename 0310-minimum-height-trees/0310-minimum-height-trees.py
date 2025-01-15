class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # modified topo sort
        if n <= 2:
            return edges
        
        indegree = [0] * n
        adjlist = defaultdict(list)
        mht = []
        
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        queue = deque(i for i in range(n) if indegree[i] == 1) # added the leaves which are far 
# trimming process continues until there are only two/one node(s) left in the graph, which are the centroids that we are looking for.
        while queue:
            mht.clear()
            curlen = len(queue)
            for _ in range(curlen):
                node = queue.popleft()
                mht.append(node)
                for nei in adjlist[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1: # last iter will store the result, centroid of the tree
                        queue.append(nei)
        
        return mht

            