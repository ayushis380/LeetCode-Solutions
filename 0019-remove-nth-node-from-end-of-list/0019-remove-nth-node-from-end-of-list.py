# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Doing in one pass : maintain n nodes btwn left and right
        # Remove the (L−n+1) th node from the beginning in the list
        dummy = ListNode(0, head)
        left = dummy
        right = dummy

        for i in range(n + 1): # now right is at dummy, so should take n+ 1 steps
            right = right.next
        
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next
        # return head # If the first node (or any node) is removed, head remains unchanged in memory, which might lead to incorrect results.
