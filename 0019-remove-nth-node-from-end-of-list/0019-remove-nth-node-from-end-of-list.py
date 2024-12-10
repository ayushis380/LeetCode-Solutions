# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # add dummy at start of head so that after all the steps, left is at (n-1) node from end
        left = dummy
        right = head

        # keep distance of (n+1) in left and right - Two pointer approach
        # move right by n times
        # left started from -1 (1 left position to head)
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next 
            right = right.next # till right reaches end
        
        # delete the node
        left.next = left.next.next
        return dummy.next 