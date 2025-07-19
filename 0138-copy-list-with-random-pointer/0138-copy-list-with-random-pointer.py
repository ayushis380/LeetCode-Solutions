"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        ptr = head
        # create interweaved list 
        while ptr:
            cpy = Node(ptr.val)
            
            cpy.next = ptr.next
            ptr.next = cpy
            ptr = ptr.next.next
        
        # assign the random pointers
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        
        # unweave the list
        old_head = head
        new_head = head.next
        result = head.next
        
        while old_head:
            old_head.next = old_head.next.next
            new_head.next = new_head.next.next if new_head.next else None

            old_head = old_head.next
            new_head = new_head.next
        
        return result