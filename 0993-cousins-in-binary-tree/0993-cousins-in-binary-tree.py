# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([root])
        
        while queue:
            cousins = False
            siblings = False
            cur_depth = len(queue)
            
            for _ in range(cur_depth):
                node = queue.popleft()
                if node is None:
                    siblings = False # boundary ended
                else:
                    if node.val == x or node.val == y:
                        if not cousins: # for the first time, set both flags as true. The flags are set as true to mark the possibility of siblings or cousins.
                            cousins, siblings = True, True
                        else: # for second time, answer depends on if they are siblings or not
                            return not siblings
                    
                    queue.append(node.left) if node.left else None
                    queue.append(node.right) if node.right else None
                    queue.append(None) # its a boundary to find the siblings, left and right with same parent are siblings
            
            if cousins: # end of a level if `cousins` is True then we found only one node at this level = Pruning step
                return False
        
        return False
