# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        result = []

        def preorder(node, r, c):
            if not node:
                return 
            
            cols[c].append((r, node.val)) # tuple row, value
            preorder(node.left, r + 1, c - 1)
            preorder(node.right, r + 1, c + 1)
        
        preorder(root, 0, 0)
        
        for i in sorted(cols.keys()):
            level = sorted(cols[i], key = lambda x : (x[0], x[1]))
            result.append([v for _, v in level])
        
        return result