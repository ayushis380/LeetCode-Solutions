# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
            return [root.val]
        
        def is_leaf(node):
            return node and not node.left and not node.right
        
        boundary = [root.val] # started from root
        # left boundary
        left = []
        curr = root.left
        while curr:
            if not is_leaf(curr):
                left.append(curr.val)
            curr = curr.left if curr.left else curr.right
        
        # leaves - we dont use queue here, it might disturb the order of leaves, right leaves might come before left
        # queue - here we add both left and right child of a node, but which node is popped first isnt guaranteed
        leaves = []
        def find_leaves(node): # this dfs func ensures we cover all left leaves then right leaves
            if not node: # if null, go to other side
                return 
            if is_leaf(node):
                leaves.append(node.val)
                return
            find_leaves(node.left)
            find_leaves(node.right)
        
        find_leaves(root)
        
        # right boundary
        right = []
        curr = root.right
        while curr:
            if not is_leaf(curr):
                right.append(curr.val)
            curr = curr.right if curr.right else curr.left
        
        right.reverse() # reverse order, going from bottom to up
        
        return boundary + left + leaves + right