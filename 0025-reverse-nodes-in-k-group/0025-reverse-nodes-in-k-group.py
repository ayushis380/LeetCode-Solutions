# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # head of list changes, so dummy is best to handle that
        groupPrev = dummy # one node before the group

        while True:
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next # one node after the group
            prev, cur = kth.next, groupPrev.next # prev is not set to None as that will break the LL into two

            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = groupPrev.next # to update the groupPrev
            groupPrev.next = kth # old head -> new head, eg dummy -> 2, 1 -> 4 
            groupPrev = tmp
        
        return dummy.next

    def getKthNode(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        
        return cur