# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            dfs(root.right)
            
            tmp = root.right
            root.right = root.left
            root.left = tmp
        
        dfs(root)
        return root