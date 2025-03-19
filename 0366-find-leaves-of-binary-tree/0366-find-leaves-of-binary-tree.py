# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
# Each node's "level" in the result corresponds to how deep it was in the tree before being removed.
        output = []

        def postorder(node):
            if not node:
                return -1 # updates height of leaf node to 0
            
            leftht = postorder(node.left)
            rightht = postorder(node.right)
            height = max(leftht, rightht) + 1 # height of each node

            if height == len(output):
                output.append([]) # create new list for this level
            
            output[height].append(node.val) # at index = height, append the values
            
            return height
        
        postorder(root)
        return output

