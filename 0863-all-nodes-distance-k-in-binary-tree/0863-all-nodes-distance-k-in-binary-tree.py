# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        rootMap = {}
        queue = deque([target])
        visited = set([target])

        def preorder(root):
            if not root:
                return
            
            if root.left:
                rootMap[root.left] = root
                preorder(root.left)
            if root.right:
                rootMap[root.right] = root
                preorder(root.right)
        
        preorder(root)

        while queue and k:
            curlen = len(queue)
            k -= 1

            for i in range(curlen):
                node = queue.popleft()

                if node in rootMap and rootMap[node] not in visited:
                    queue.append(rootMap[node])
                    visited.add(rootMap[node])

                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)

                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
        
        # return list(queue)
        return [node.val for node in queue]
