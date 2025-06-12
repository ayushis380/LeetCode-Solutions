# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # insert a new node as a child of the leaf
        # Both tc and sc : O(H), where H is a tree height. That results in O(logN) in the average case, and O(N) in the worst case.

        if not root:
            return TreeNode(val) # when find the next empty child position, return this node
        
        if val > root.val:
            # assignment is necessary
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        return root