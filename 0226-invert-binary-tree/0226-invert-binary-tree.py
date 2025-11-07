# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def dfs(root):
            if not root:
                return 
            
            lefts = dfs(root.left)
            rights = dfs(root.right)

            root.left = rights
            root.right = lefts
            return root
        
        return dfs(root)