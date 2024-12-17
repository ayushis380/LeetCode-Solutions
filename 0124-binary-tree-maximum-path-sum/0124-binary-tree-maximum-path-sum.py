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
            
            leftsum = dfs(root.left)
            rightsum = dfs(root.right)

            maxsum = max(maxsum, leftsum + rightsum + root.val)
            return max(leftsum + root.val, rightsum + root.val, 0)

        dfs(root)
        return maxsum