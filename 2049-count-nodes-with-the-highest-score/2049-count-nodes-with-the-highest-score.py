class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
    # if a node has a parent and two children then there can be max 3 sub trees formed
    # Find left, right, up (number of nodes) for each node
        n = len(parents)
        adj = defaultdict(list)
        self.maxScore = 0
        self.count = 0

        for i, p in enumerate(parents): # build graph
            if p != -1:
                adj[p].append(i)
        
        # Step 2: DFS function to calculate subtree sizes and node scores
        def post_order(node):
            total = 1 # count current node
            score = 1

            for child in adj[node]: # go through all child nodes 
                size = post_order(child) 
                total += size
                score *= size # multiply sizes of each child subtree
            
            remaining = n - total # n - 1 - left - right,  # rest of the tree if current node is removed

            if remaining > 0: # when remaining == 0 then we are at root of tree, and score already has leftsize * rightsize
                score *= remaining # leftsize * rightsize * remaining 
            
            if score > self.maxScore:
                self.maxScore = score
                self.count = 1
            elif score == self.maxScore:
                self.count += 1
            
            return total # each node is counted as 1, this returns node + left size + right size
        
        post_order(0)
        return self.count
