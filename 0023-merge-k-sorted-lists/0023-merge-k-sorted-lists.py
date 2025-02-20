# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        heap = []

        for i, ls in enumerate(lists):
            if ls:
                heapq.heappush(heap, (ls.val, i, ls))

        while heap:
            val, i, ls = heapq.heappop(heap)
            node = ListNode(val)
            cur.next = node
            cur = node

            if ls.next:
                heapq.heappush(heap, (ls.next.val, i, ls.next))
        
        return dummy.next