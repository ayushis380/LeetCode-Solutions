# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode()
        cur = head
        heap = []

        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst)) # we need i for cases when ListNodes values are same, then heap checks on basis of i; otherwise ListNode (lst) would have been compared which is invalid
        
        while heap:
            val, i, lst = heapq.heappop(heap)

            node = ListNode(val)
            cur.next = node
            cur = node

            if lst.next:
                heapq.heappush(heap, (lst.next.val, i, lst.next))
        
        return head.next

