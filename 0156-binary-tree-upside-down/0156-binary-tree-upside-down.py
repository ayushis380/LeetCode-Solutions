# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root  # Base case
        
        # Recurse to find new root
        new_root = self.upsideDownBinaryTree(root.left)
        
        # Rotate tree nodes, root.left is the new parent node, so add references to it
        root.left.left = root.right  # Old right becomes new left
        root.left.right = root  # Old root becomes new right
        
        # Detach original root from its children
        root.left = None
        root.right = None
        
        return new_root