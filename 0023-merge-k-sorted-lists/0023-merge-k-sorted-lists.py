# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        interval = 1
        n = len(lists)

        while interval < n:
            for i in range(0, n - interval, interval * 2):
                print("i is ", i)
                lists[i] = self.merge(lists[i], lists[i + interval])
            
            interval *= 2
        
        return lists[0] if n > 0 else None
    
    def merge(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        cur.next = l1 if l1 is not None else l2
        return dummy.next