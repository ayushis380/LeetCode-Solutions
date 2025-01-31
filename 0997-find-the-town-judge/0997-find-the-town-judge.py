class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int) # for indegree and outdegree

        for src, dst in trust:
            delta[src] -= 1
            delta[dst] += 1
        
        # for p_id, val in delta.items(): # fails when n = 1 and trust = []
        #     if val == (n-1): 
        #         return p_id

        for i in range(1, n + 1):
            if delta[i] == n - 1: # everyone except judge trust judge 
                return i
        
        return -1