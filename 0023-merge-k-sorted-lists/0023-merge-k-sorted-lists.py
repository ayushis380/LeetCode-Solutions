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
        for ind, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, ind, node))
        dummy = ListNode(0)
        cur = dummy 

        while heap:
            val, ind, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, ind, node.next))
        
        return dummy.next