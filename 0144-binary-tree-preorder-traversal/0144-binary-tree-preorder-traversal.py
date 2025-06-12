# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Top->Bottom and Left->Right
        if not root:
            return []
        
        stack, result = [root], []

        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                if node.right: # right added before so its popped afterwards
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return result