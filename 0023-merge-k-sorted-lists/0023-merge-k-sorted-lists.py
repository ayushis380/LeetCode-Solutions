# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        heap = []
        dummy = ListNode(-1)
        cur = dummy

        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))
        
        while heap:
            val, i, lst = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next

            if lst.next:
                heapq.heappush(heap, (lst.next.val, i, lst.next))
        
        return dummy.next
