# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        colMap = defaultdict(list)
        result = []

        def traversal(node, r, c):
            if not node:
                return 
            
            colMap[c].append((r, node.val))
            if node.left:
                traversal(node.left, r + 1, c - 1)
            if node.right:
                traversal(node.right, r + 1, c + 1)
        
        traversal(root, 0, 0)
        mincol = min([key for key in colMap.keys()])
        maxcol = max([key for key in colMap.keys()])
        print(mincol)
        print(maxcol)

        for col in range(mincol, maxcol + 1):
            # temp = colMap[col]
            # print(temp)
            result.append([val for r, val in sorted(colMap[col])])
        
        return result
