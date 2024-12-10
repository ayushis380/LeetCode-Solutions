# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next # start of second half
        prev = slow.next = None # first half ends at slow so slow.next is set to None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge first and second(reversed) half
        first, second = head, prev # prev becomes the head of reversed second half
        while second: # first and second will be of same size when even, second will be shorter when odd
            tmp1, tmp2 = first.next, second.next # storing next vals before we break links
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2