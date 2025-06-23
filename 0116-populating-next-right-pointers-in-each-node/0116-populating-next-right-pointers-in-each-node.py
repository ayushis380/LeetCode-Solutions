"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # at every level, we are connecting the children of that level
        # using BFS without extra space
        cur, nxt = root, root.left if root else None # start and next level start(left most)

        while cur and nxt:
            cur.left.next = cur.right
            if cur.next: # 2 has 3 as next
                cur.right.next = cur.next.left # to link 5 to 6 in eg 1
            
            cur = cur.next # next node at current level, like a BFS
            if not cur: # reached the end, eg after 3 there is nothing
                cur = nxt # replace cur and nxt
                nxt = cur.left # start of next level from left most
        
        return root
