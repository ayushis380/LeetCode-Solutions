class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        tree = defaultdict(list)
        
        # Step 1: Build the tree using adjacency list
        for child, parent in enumerate(parents):
            if parent != -1:
                tree[parent].append(child)

        self.max_score = 0
        self.count = 0

        # Step 2: DFS function to calculate subtree sizes and node scores
        def dfs(node):
            total = 1  # count current node
            score = 1
            for child in tree[node]:
                sz = dfs(child)
                total += sz
                score *= sz  # multiply sizes of each child subtree
            
            remaining = n - total  # rest of the tree if current node is removed
            
            if remaining > 0:
                score *= remaining
            
            if score > self.max_score:
                self.max_score = score
                self.count = 1
            elif score == self.max_score:
                self.count += 1
            return total

        dfs(0)
        return self.count