# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
# root node has a column index of 0, then its left child node would have a column index of -1 and its right child node would have a column index of +1
# the nodes should be ordered by column first, and further the nodes on the same column should be ordered vertically based on their row indices
        if not root:
            return []
        
        queue = deque([(root, 0)]) # node, col
        colMap = defaultdict(list)
        minCol, maxCol = 0, 0
        result = []

        while queue: # bfs helps in getting the values row wise and from left to right, as needed for result
            node, col = queue.popleft()
            colMap[col].append(node.val)
            
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)

            if node.left:
                queue.append((node.left, col -1))
            if node.right:
                queue.append((node.right, col + 1))
        
        # arrange them in column order 
        for col in range(minCol, maxCol + 1):
            result.append(colMap[col])
        
        return result