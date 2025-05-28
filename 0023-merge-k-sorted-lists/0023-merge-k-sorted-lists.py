# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        interval = 1

# interval * 2 is used to control the gap between pairs being merged, and it doubles each iteration to reduce the number of lists logarithmically
# i jumps by interval * 2 because each merge operation combines two intervals of length interval

        while interval < length:
            for i in range(0, length - interval, interval * 2):
                print("i is ", i)
                lists[i] = self.mergeTwoLists(lists[i], lists[i+interval])
            
            interval *= 2 # less steps in next iteration 
        
        return lists[0] if length > 0 else None
    
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        cur = head 
# not creating new nodes in this approach - its just placing the pointers in right way

        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            
            cur = cur.next
        
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        
        return head.next