# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        cur = root
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root # root is returned, not cur
                cur = cur.right # keep on checking till we get a child pos to insert
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left