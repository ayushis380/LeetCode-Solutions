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
        dummy = ListNode()
        cur = dummy

        for i, ls in enumerate(lists):
            if ls:
                heapq.heappush(heap, (ls.val, i, ls))
        
        while heap:
            val, ind, ls = heapq.heappop(heap)
            node = ListNode(val)
            cur.next = node
            cur = node

            if ls.next:
                heapq.heappush(heap, (ls.next.val, ind, ls.next))
        
        return dummy.next