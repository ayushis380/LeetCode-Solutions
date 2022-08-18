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
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null)
            return head;
        ListNode ptr = reverseList(head.next);
        head.next.next = head; // reversed the link now two nodes are pointing to each other
        head.next = null; // need to break the old link;
        return ptr; // new head of the reversed linked list
    }
}