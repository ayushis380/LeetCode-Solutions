# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy  # create a diff of +1
        right = head

        while n > 0 and right: # move n steps
            right = right.next
            n -= 1
        
        while right: # right and left has a distance of n nodes which places left at n -1 node which makes it easier to remove nth node from end
            right = right.next
            left = left.next # left starts late with +1 extra node
        
        left.next = left.next.next
        return dummy.next