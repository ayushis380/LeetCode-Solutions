# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # pair : [withroot, withoutroot]
        def dfs(root):
            if not root:
                return [0, 0]
            
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            withRoot = root.val + leftPair[1] + rightPair[1] # pick root val and its children without root values, as we have picked root val here so we cant pick its children values but the value which doesnt take their node values
            withoutRoot = max(leftPair) + max(rightPair) # always pick max from both sides, can be possible that we pick children of children node values 

            return [withRoot, withoutRoot]
        
        return max(dfs(root))