"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        dummy = Node(0)
        cur = dummy 
        stack = [head] # add node.next and then node.child so that child value is popped first 

        while stack:
            tmp = stack.pop()
            if tmp.next:
                stack.append(tmp.next) # added before, we need to start back from here
            if tmp.child:
                stack.append(tmp.child) # need to be processed before
            
            cur.next = tmp
            tmp.prev = cur
            tmp.child = None # asked in ques to set
            cur = tmp
        
        dummy.next.prev = None # head.prev = None
        return dummy.next # head