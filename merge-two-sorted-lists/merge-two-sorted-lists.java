/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode res= dummy;
        while(list1!= null && list2 != null){
            int small = list1.val> list2.val ? list2.val : list1.val;
            ListNode temp = new ListNode(small);
            res.next = temp;
            res = res.next;
            if(small == list1.val) 
                list1 = list1.next;
            else 
                list2 = list2.next;
        }
        if(list1!= null)
            res.next = list1;
        if(list2!= null)
            res.next = list2;
        return dummy.next;
    }
}