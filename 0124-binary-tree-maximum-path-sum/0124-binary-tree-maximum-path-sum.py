# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float("-inf")

        def dfs(node):
            nonlocal maxsum

            if not node:
                return 0
            
            lsub = dfs(node.left)
            rsub = dfs(node.right)

            sumval = lsub + rsub + node.val
            maxsum = max(maxsum, sumval)
            return max(lsub + node.val, rsub + node.val, 0)
        
        dfs(root)

        return maxsum