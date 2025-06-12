# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
        # replace the value with either of the sides if other is not present
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            cur = root.right # otherwise, go to right's minimum value as it will keep the BST valid
            while cur.left: # don't want it to go till None
                cur = cur.left
            
            root.val = cur.val # replace the value
            root.right = self.deleteNode(root.right, root.val) # delete the duplicate node taken from right side (replacement)
        
        return root
