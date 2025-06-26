class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        cur = root  # Start with the current level's head
        
        while cur:
            dummy = Node(0)  # Dummy head for the next level
            tail = dummy     # Tail to build the next level
            
            # Traverse the current level
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next  # Move within the current level
            
            # Move to the next level
            cur = dummy.next
        
        return root
