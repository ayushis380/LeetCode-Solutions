# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float("-inf")

        def dfs(root):
            nonlocal maxsum
            if not root:
                return 0
            
            lefts = dfs(root.left)
            rights = dfs(root.right)

            maxsum = max(maxsum, root.val + lefts + rights)
            return max(root.val + lefts, root.val + rights, 0)

        dfs(root)
        return maxsum