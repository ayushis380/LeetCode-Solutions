# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def dfs(root):
            nonlocal max_len
            # Post order traversal as we need to make decision after we have values from left and right
            if root == None:
                return 0
            left_len = dfs(root.left)
            right_len = dfs(root.right)

            left_arrow = right_arrow = 0

            if root.left and root.val == root.left.val:
                left_arrow = 1 + left_len 
            
            if root.right and root.right.val == root.val:
                right_arrow = 1 + right_len
            
            max_len = max(max_len, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
        
        dfs(root)
        return max_len